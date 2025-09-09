---
title: "HyperLogLog: magical (kind of) unique counters"
description: 
date: 2025-09-08T20:08:22+02:00
image: 
math: 
slug: hyperloglog
license: 
hidden: false
comments: true
draft: false
---

> **TL;DR**
> [HyperLogLogs](https://en.wikipedia.org/wiki/HyperLogLog) (hll) can be a replacement for a set when only the number of unique elements (cardinality) is needed, **and an approximation is enough**.
>
> It is a very efficient structure both in time (`add` is `O(1)`) and space (fixed size typically ~12KB, depending on the desired error rate).
>
> Moreover, two hll can be **merged very efficiently ($O(1)$)**, with no loss of precision.


## The problem

### A simplification

Imagine you are a store owner, and you want to count how many unique customers you get each day.
Simple enough, you only need some pen and a piece of paper.
Every time a customer walks in, you check whether their name is already on your paper[^1].
If it is, you don't need to do anything.
If it isn't, you add it.

[^1] You're a great store keeper, so you know every single customer by name!

At the end of the day, you simply count the number of names in your paper to get your answer.

One problem you may find is that checking whether a customer is already in the list can be slow, and you may not be able to keep up with the ludicrous thoroughput of customers to your successful store.
There are some tricks to alleviate this:

* Sorting. Keeping your list of names always sorted. This can be very difficult with pen and paper :)
* Partitioning. Separating your clients by some criteria (e.g., first letter in their surname) and assigning a portion of your paper for each possible value. You may repeat this process for each portion.
* Deferring deduplication. Write their names every time, and wait until a later time to check if you have already seen them. That later time can be a less busy moment of the day, or some time after the day is over.


The second problem is that the list of users

In a programming context, the first problem translate to time complexity.
The typical approach is to have something like a a hash set.
That makes checking very fast ($O(1)$).
Adding a new name is also fast, unless the set needs to grow (amortized $O(1)$).
A drawback is that hash sets need to be reasonably empty to work as intended, so we are trading speed for space.

The second problem translates to memory utilization.
If each name has a length of $l$ bytes, and we have a total number of $u$ unique users, we would need **at least** $l \times u$ bytes, so $O(l \times u)$.
For simplification, we can express $u$ as a product of how many times customers enter the store ($n$) and the ratio ($r$) of those visits that are from a unique customer: $u = n * r$.

### The real problem

You are such a great owner that your business has grown and you now have ten ($10$) more stores in town.
Naturally, you want to see how each of the ten locations is doing, and you want to keep track of how unique customers your business has as a whole.
So you need to:

- Keep a record of each individual store. In our case, that would mean $10$ times more total records.
- Somehow merge the records from each location into one. If we have two counters, we need to go through all the elements of the smallest one, and add them to the bigger one. (plus optionally copying the biggest counter or starting anew and adding both to avoid modifying it)

This compounds the problems from the previous section:

- Each store does roughly the same, so the time and space needed grow $s$ times (for $s$ stores). 
- To merge the counters, we roughly need to go through each unique customer of each store.
- We need to store the result. Depending on how many repetitions from store to store you get, this can go from as big as your biggest counter (all others are contained), up to the sum of all the counters (no repetition).


So, in summary, assuming we can insert with $O(1)$ and we get on average $n$ customers per store, we need roughly:

- $O(s \times n)$ operations to get unique customers for every store.
- $O(s \times n \times r)$ operations to join them.
- $O((s+1) \times n \times r \times l)$ total space to save all of this information.

The two key factores here are that:

- Space grows linearly with the number of unique customers $n \times r$
- Space grows lineraly with the number of stores ($s$)
- Space grows linearly with the size of the key we are storing ($l$, length of names)
- Merging time grows linearly with the number of stores ($s$)
- Merging time grows linearly with the number of members in each counter ($n \times r$)

## Enter HyperLogLog

Let's look at a simpler problem before we explain the hyperlog.

Imagine you toss a coin until you get tails (or up to 100 throws).
How likely are you to draw a sequence of at least 10 heads?
For a fair coin, the probability of that event would be $1/2^{10}$
And 5 heads?
$1/2^5$.
And, in general, $1/2^h$, for $h$ heads.

We can flip the problem on its head (pun intended).
Let's say I repeat the same coin tossing multiple times, each time stopping when I get tails.
If I tell you I got **at most** 10 heads and tell you to guess **how many tails I got** (i.e., total sequences), what would you say?

A naive answer would be that, in order to get an event with $1/2^10$ chance, I probably did about $2^10$ attempts.
Much fewer or much more, and I would have gotten a different number.

> [!Warning]
> This part is based on my (limited) understanding of the math behind HLL.
> Please, take it with a grain of salt, and feel free to correct me.

The problem with this approach is that it produces very rough estimates (see the [Flajolet–Martin algorithm](https://en.wikipedia.org/wiki/Flajolet%E2%80%93Martin_algorithm), especially for higher values of $h$.

The key idea behind HyperLogLog is that, instead of keeping track of a single number, we separate our attempts into multiple groups (registers).
Say, $m$ registers (for maxima).
The first attempt affects the first register, the second the second one, and so on, until we run out of registers and we start again.
Then, we get $m$ estimates of $n\_attempts / m$.
It turns out using the harmonic mean of all the attempts and multiplying it by $m$ is a great estimate of the total number!

Could we use the same idea to solve our original problem?
We only need a way to transform our input (the names) into a set of tosses.
The output has to be deterministic (to work as a unique detector), uniform (assumption).

But that is precisely the definition of a hashing function!
It turns an input into a series of ones and zeros of a fixed length.
And the distribution of values of a good hashing function should be uniform in order to minimize collisions.

We can turn a hash into a sequence of tosses by keeping only the leading part up to the first 1.

Actually, another practical difference is that, instead of doing a round robin selection of registers, we will use part of the hash to select which register to update.
The distribution of values should still be uniform, and we eliminate the need to keep a counter.
So, we use just enough bits from the beginning to select the register ($log_2(m)$ for $m$ registers), and we convert the rest into a sequence.

It turns out that counting the number of leading zeros (most significant bit) is very fast on modern computers due to hardware support.
And, no, that is not a coincidence.

In practical terms, we also need to apply some correction correct for hashing collisions.

Another practical difference is that there are hashing collisions. between  and multiple hashes that start with the same sequence of zeros (and a one).


That means that, a HLL has $m$ registers (maxima), and for each element that is added it:

- Calculates a hash of each element (to get a uniform distribution and a fixed size)
- Assigns the element to one of the $R$ registers, $j$, based on the head of that hash (first $log_2(R)$ bits).
- Counts $z$, the number of leading zeros in the tail of the hash
- Increments the maximum in that register ($M[j] = max(z, M[j])$

To get an estimate of the cardinality we have three situations:

- The HLL does not have enough elements: $V > 0$, where $V$ is the number of zero elements. We use linear Counting ($E = m \times log( m / V))$)
- The HLL has enough elements. We estimate the cardinality $E$ as: $E = m \times harmonic\_mean(M) \times c$. Where $c$ is a factor that corrects for hash collisions.
- The HLL has too many elements. In this case, we need to correct the estimate from the second case. 

The error of our estimation will be a function of the number of registers: $sigma = 1.04 / sqrt(m)$.

To merge two HLLs with the same number of registers and hashing functions, you only need to compare each register position, and get the maximum of the two values.
This operation is very fast ($O(m)$, which is small in practice).
There is also no loss of relative precision.


Going back to our original problem, we will analyze the effect of using HLLs to estimate each the number of unique customers in each store.
If we assume our hashing is $O(1)$ and we get on average $n$ customers per store, we get roughly:

- $O(s \times n)$ operations to get each store's unique customers
- $O(s \times m)$ operations to join them. Where $m$ is the number of registers in each HLL.
- $O((s+1) \times m)$ total space to save all of this information.

Hence, compared to our solution using sets:

- **Space ~grows linearly with~ does not depend on the number of unique customers**
- Space grows lineraly with the number of stores ($m$)
- **Space ~grows linearly with~ does not depend on the size of the key we are storing ($l$)**
- Space depends linearly with the number of buckets, which is a function of the precision/error rate
- Merging time grows linearly with the number of stores ($m$)
- **Merging time ~grows linearly with~ does not depend on the number of members in each counter ($n$)**


## Drawbacks

As magical as HLLs are, there are some caveats:

- The cardinality provided is an **estimation** up to an **error_rate**, usually in the rage of 1-2%
- In order to merge two HLLs, they need to have:
  - The same number of registers
  - The same hash function
- HyperLogLogs are append-only. You cannot remove elements
- You cannot calculate the difference of two HLLs (but you can calculate its cardinality)


## Additional properties

- The result of merging two HLLs has the same **error_rate** 
- It is possible to calculate the cardinality of:
    - the difference of two HLLs ($cardinality(a - b) = cardinality(a ∪ b) - cardinality(b)$)
    - the intersection of two HLLs ($cardinality(a ∩ b) = cardinality(a) + cardinality(b) - cardinality(a ∪ b)$)

## SlidingHyperLogLog

There are some really neat variations over HLLs for specific use cases.
One I am specially interested in is the SlidingHyperLogLog, which can calculate the cardinality of events over a rolling window.
An application of this would be to keep counters of unique IPs seen on a network over the past $W$ minutes.

Since HLL are only additive, it is not possible to apply the typical approach in sliding windows of removing old elements that are no longer within the window.
The naive solution to get a Sliding Window counter of width $W$ ould be be to get all events that happened in the past $W$ minutes and construct a HLL with them.
You would need to do that every $T$ minutes or for every incoming event, depending on your strategy/needs.
That is unnecessarily wasteful.
Imagine having a window of $W=120$ minutes with a resolution of $T=1$ minute.

Instead, the SlidingHyperLogLog exploits the fact that HLLs only keep track of the maximum count in each register.
The intuition is that, when we add an element at time $t$ with count $V$ and belonging to register $r$, we can:

- Forget any elements in register $r$ that:
    - Were added before $t-W$
    - Had a count $<=V$
- Add this event and time ($(t, V)$) to a list of values for the register
- Update the count in the register to the maximum of all the remaining elements

Using some clever data structures (e.g., a binary heap) and algorithms, we can very efficiently perform the insertion and removal of events.


## Python

For now, I've only used the [HyperLogLog](https://github.com/svpcom/hyperloglog/) library, which is a python implementation that relies on $numpy$:

```python
!pip install hyperloglog

from hyperloglog import HyperLogLog

h = HyperLogLog(error_rate=0.01)

h.add("Hello from my blog")

print(len(h))
```
