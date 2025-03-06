---
title: "Tips for efficient collaboration"
slug: efficient-collaboration
description: 
date: 2025-03-05T09:25:54+01:00
image: 
math: 
license: 
hidden: false
comments: true
draft: false
---

## Background 

> TL;DR I work in academia. This post focuses on advice I'd give a younger me to be a more effective supervisor and project lead.
{ .note }

My role in my research group has evolved from individual contributor to project lead that manages a team of multiple students.
This often involves coordinatating with other senior researchers and their teams.

This post is a collection of advice I would have given myself back when I started this journey.
It is also an excuse to reflect on these ideas I've been implicitly applying everyday, and maybe learn a few things more in the process.

In my field, projects are often tied to a specific grant or some sort of public funding.
This means that the main concern of the lead is to ensure that the results at the end of the project match the description in the project proposal.
It also typically means maximizing the number of publications related to the project and their overall impact.

To do so, most projects rely on three types of staff: a) senior researchers (post-doc); b) junior researchers (PhD students); and c) interns doing their bachelor's or master's thesis.
The level of contribution is generally inversely propotional to the level of mastery of the contributor: PhD students design and develop the main contributions (both software and experimental) under the supervision of senior researchers (advisor/supervisor), and interns take care of tasks that are narrow in scope and not crucial to any academic contribution.
For instance, a PhD student may develop a new model for text classification, and an intern will wrap that model in an HTTP service with a nice UI.
When the service and UI part is intricate and has some potential academic merit, that task may be conducted by a PhD student as part of their thesis.
That was precisely the case with Senpy, which was part of my PhD thesis, and it has since been used by dozens of students to develop services in the context of other research projects.


## Reasons to form a team

In my opinion, a team has two advantages over a single contributor.
The first one is that collaboration often generates **synergies**, leading to surprising and enriching results (a team is greater than the sum of its parts)
Carefully selecting your team members and creating an environment that is conducing to these synergies is a topic on its own, and I will not get too deep into it here.

The second advantage can be summarized as **concurrency**: tasks can be tackled by more than one member.
This often implies some sort of parallelism.
Tasks tend to be split between different members, in hopes of speeding up the process.
But it can also be beneficial to have concurrency even in the absence of parallelism: different members can take turns solving the same problem.
This is common when the task requires exclusive access to a resource (e.g., performing an experiment on an expensive machine).

## Challenges of teams (of students)

Just like in computer science, coordination in a concurrent project involves a non-negligible overhead.
The objective is to minimize this overhead.

I've really struggled with managing teams in the past.
Given my context, I often attributed the failures to lack of time (having to juggle teaching and research), lack of training and preparation on the intern's side (they're often undergrads), lack of appeal or definition of the task (too academic-y), or any other external factors. 

While all those aspects play an important role, some of them are out of our control as a project lead in academia: grants require a certain type of project and workflow, and the quality of our interns is bounded by the quality of our degrees.
So I think it is more constructive to focus on things that we can control.
In other words: we have to play the hand we're given.

Besides, there is no merit in achieving good results with excellent students/engineers.
They would succeed on their own even if you weren't there.
The real test for a good leader is succeeding with a subpar team.


In that vein, I've reflected on my mistakes as a leader, and the inefficiencies of the teams around me.
I'd classify my failures in the following areas:

* Delegation (and lack thereof). Piling up too many tasks and blocking progress.
* Communication. Not having a coherent view of the state of affairs, the details of specific tasks, the general processes to follow, or the priorities of different tasks within a project.
* Direction (or purpose). Not having a common direction

### Delegation

I have a tendency to become a bottleneck in any project I am involved in: many tasks end up depending on me, either directly or indirectly. In the concurrency metaphor, I become a lock for many tasks, and a single executor for the rest.
This issue was not that apparent early on, when most of my work was as an individual contributor or I had the bandwidth to supervise and complete my tasks.

I think it is quite common to feel like delegating a task in these scenarios means:

1. Defining the task in advance
2. Choosing an assignee for the task
3. Setting a deadline for the task
4. Explaining the task and the relevant context
5. Replying to multiple questions by e-mail or in person. Extra points when the questions make you wonder if any part of the explanation was ever clear.
6. Reviewing the results after the deadline
7. Realizing the assignee misunderstood the task or delivered something not even close to what you agreed upon
8. Going back to point 3.
9. When you're unlucky or short on time: giving up and doing the task yourself

Many times, if felt like delegating tasks only lead to frustration and wasted time.
Especially when compared to the alternative:

* Defining the task
* Setting a deadline
* Finishing the task
* Profit

Luckily, some students and projects were an exception to this.
They worked autonomously and delivered something beyond the minimum requirements.
This reinforced my helplessness and the feeling that the problem was not being able to work with experienced engineers.

However, I now believe that the truth lies somewhere in between.
Sometimes your circumstances make it quite hard or inefficient to delegate tasks.
And some times may not be good candidates for delegation.
But most of the times you can take advantage of having an extra pair of hands, you just have to do that effectively.

### Communication

Small teams rely on implicit knowledge more than they realize.
Even more so if the team is made up of highly specialized people that have worked in the same environment with mostly the same people for years.

Communication is a broad term.
It includes technical and concrete things such as how a certain task should be done.
But it also includes broader things like etiquette, organizational values, and who is more willing to help you out on certain topics on a Friday afternoon.

Here, I would take a page out of Python's zen and recommend that "explicit is better than implicit".
Implicit (or tacit) knowledge comes with a whole set of drawbacks:

* It makes onboarding new users harder. Without a common knowledge base, all knowledge transference has to rely on personal interactions. Even worse, those interactions are probably organized on the spot, and are likely to miss important points.
* It makes you heavily reliant on your current members (and their memory).
* It impedes proper evaluationn and progress, since they are not written anywhere.
* It increases the likelihood of misunderstandings when two members have conflicting beliefs, and makes it harder to detect them until it is too late.
* It makes contradictions and (unknowingly) changing your mind much more likely. It can happen to the best of us, especially if you are involved in too many projects. When contraditions happen often, your colleagues will learn not to rely on your opinion.

On the other hand, communication has to go both ways.
This means that your newer members need to be able to communicate when something is going wrong or can be improved (backpressure).
They should also feel free to talk about their motivation, state of mind, and feelings, **when appropriate**.
That last part is quite subjective, of course.
Try to find your - and your organization's - middle ground between "I don't care how you feel, just do your job" and "sure, you can go to the Maldives on short notice. Oh, and don't worry about not having met a deadline in months, I'm sure you're stressed and can use some vacation but will work remotely if we need you".

I personally feel a sweet spot is treating your coworkers like people, being empathetic and compassionate.
Part of being a good coworker is fulfilling the duties and obligations you accepted when signing your contract.
First and foremost, because not fulfilling them means someone else will have to work harder to make up for it.
And, secondly, because doing our part is the only way to move the organization (and research) forward.

### Direction

By failure in direction I mean not keeping a consistent and shared set of general goals, principles and values in your organization.
In order to really take part in any enterprise, you need to have a clear understanding of the objectives and motivation.
When it comes to specific tasks, *what you're doing* is often not as important as the *why you're doing it*.
In fact, there may be times where you aren't truly sure of what exactly it is that you are doing, but you trust the process and the motivation behind the task.

I've seen two failure modes in this regard.
The first one is to not have a clear direction.
The end result is that members of the team are not really that committed.
If no other *why* is provided, we are only left with *because they pay me to do it*.
And academia is not known to pay particularly well, to be honest.

The other mode is to provide contradicting or incompatible directions.
This can be in a short period of time, leading to the impression that there isn't really any conviction in the message.
But it can also be done over a longer period of time.
That can be perfectly acceptable, provided that the change in direction is justified and compatible with the principles of the organization.


Failure in direction is somewhat related to communication, but it subtly different.
An organization can excel at communication, but change their direction constantly.
Arguably, a thorough communication strategy makes radical changes in direction less likely.
On the one hand, a change in direction needs to be documented, which can be a pain.
On the other hand, a written change is easier to spot and more likely to generate complaints.


## Rules

I'd argue that the path to successfully managing a research team lies in roughly the following key goals:

* Fostering autonomy
* Avoiding miscommunication
* Optimizing your contribution
* Coordinating with other teams
* Creating a team

The remaining of the post will be a series of tasks or rules to achieve these goals.

> Most of these ideas probably generalize well to collaboration outside of academia, but I hesitate to make more general claims.
{.warning}

### Fostering automony

The tips here are aimed at avoiding supervision overhead and training future leads.

#### Provide a (simplified version of the) bigger picture

Try to paint the bigger picture, even for menial tasks within large projects.
For you, this may be the nth project you're involved in this year, but the new intern may not have even heard about European projects before.
Going back to the idea of direction, it is easier to work on something if you know the context of your work.

Having a general idea of the project and the context of your task will also help you make decisions on your own.
For instance, if I am told to develop a shiny new API for text classification, I may have to ask many questions: 1) what will be input look like?; 2) what should the parameters be?; 3) am I using POST or GET requests?; 4) should I return a JSON object or an XML?...
What if, instead of that, I am also told this API will be used in the context of project X, that our organization will be the only consumers of the API, and they also give me a link to the project's docs.
I may be able to figure out some of those answers on my own (e.g., by finding examples in the project's website), or decide that some questions are not vital at this point (e.g., if we are the only consumers, we can change from GET to POST if we need to much more easily).

One caveat here is that a link to the documentation or some vague words about the project do not constitute proper context.
You are responsible for summarizing the important bits of the context, providing instructions on how to navigate the reference materials, and being open to answer questions that may arise in the exchange.

#### Do not discuss implementation details unless strictly necessary

There is a fine line between discussing a non-trivial implementation detail and bikeshedding for hours about class names and code best practices.
For that reason, you should try to prioritize discussing high-level parts of the problem and the assignment, and trust the student to figure out the details on their own, or come back to you for clarification.

It is very common that students focus on very specific details when they are sharing their progress with their supervisors.
They will generally try to start by showing snippets of code and their results.
I find it helpful to remind them to explain their problems top-to-bottom, starting with a sentence or two about the context of their project, the description and motivation of the specific task they were doing, and the relationship with previous (and future) tasks.
That usually helps figure out the level of understanding of the student, whether there are any conceptual errors, and whether the specific block or problem is really worth discussing during the meeting.

Some technical problems will warrant a discussion in detail, either due to their complexity or their importance to the project.
In those cases, always limit the time you will spend on that specific issue ahead of time, and make sure to allow for some time at the end of the meeting to go back to any important high-level details.

If there are other students that worked on similar projects, do not hesitate to refer your new student to them.
It can be an opportunity for them to collaborate, and for the original student to work on explaining and teaching technical issues.

#### Provide feedback

Make a point of evaluating the results of each student on every level, and provide constructive and actionable feedback to them.
Even if no technical issues arise during the project, try to review the code and give some tips (e.g., formatting, code structure, DRY).
Try to focus on bigger issues and enforcing best practices before nitpicking and giving feedback on small subjective improvements.

Make it clear when your feedback is objective/best practice (e.g., a function is deprecated) and when it is a matter of preference.
If it is the latter, try to provide more than one alternative, to encourage them to think about it and make an educated decision.


#### Take documentation and knowledge transfer seriously

Taking the time to write down basic documentation can save a lot of time in the long run.
Besides, most of the job of mentoring a new student is lost when that student finishes their degree and leaves to find a job in industry.
Good documentation can remain in your organization and be extended long after the intern is gone.


This is very obvious for specific tools, whether internal or public.
Good documentation means any new member can check the tool and use it without much assistance.
Even better documentation helps newcomers contribute to the tool.
Make sure to make it clear who to approach if something is missing from the documentation, and make it easier to do so than to make assumptions and use the tool incorrectly.

Writing documentation can be very time consuming, and sometimes it is hard to know exactly what things to focus on when writing the docs.
You need to anticipate the needs of the future user.
If you are short on time, a good strategy is to delegate the writing of the documentation.
Instead of going into details, you can write a very barebones version and training a new user to use and contribute to your tool.
Then, leave it up to the new user to extend the documentation, including more details and pitfalls.
As a bonus, reading and fixing the docs will give you a better sense of how well that new user understands the tool, as well as possible improvements.

This tip also applies to more general areas such as machine learning, graph neural networks, or simulation.
Just remember you do not need to reinvent the wheel in those cases.
A simple summary and a list of references to expand on the topic could be more than enough.
Make sure to also include any specifics that apply to your organization.
For instance, point to repositories on github (public or private) that can be used to explore the topic, examples of similar projects in the domain, etc.

Identify what information is important for any new hire and present it to them as clearly as possible.
Part of that information should be where and how common knowledge is stored and shared, should they need more information in the future.
Make this documentation as easy to discover and consume as possible.
Centralizing this common information in the form of a wiki is often a good idea.

Lastly, make it easy for any member of your organization to update this common documentation, and encourage them to do so.
Whenever a member asks you something useful that is not documented, don't just answer the question.
Take the time to add this information yourself (e.g., by copy-pasting your response) or task that member with expanding the documentation themselves once they find an answer.
If your organization's culture does not encourage using these docs, they will quickly get outdated and fall out of use.


#### Trust your teammate's ability to learn

I've been bitten by this way too many times.
Your students are probably more capable of learning than you think, especially if you have set up your documentation right.
What they lack in experience, they make up for with free time, a (more) neuroplasticity and determination.

Sure, they will make mistakes (see the next section) and need some feedback (two sections above), but that is how we all learnt.

#### Don't be a perfectionist

Perfect is the enemy of done.
It is also the enemy of a happy co-worker.

Try to remember that you are dealing with students, and you were probably no better at their age.
Besides, you probably delegated the task beause you did not have any spare time to do it yourself.
`FIXME` is often better than `TODO`.

Take the opportunity to provide some feedback and teach them something useful.
Some mistakes are also worth adding to your documentation, or presenting to other students in a presentation.

### Avoiding miscommunication

A common source of wasted effort and unnecessary back-and-forth is miscommunication.
These are some tips to help keep everyone on the team informed and aligned.

#### Make priorities clear

All team members should understand the general priorities (project-wise) as well as the specific prorities of their assigned tasks.
This will help inform their decisions when some other tasks inevitably come up, or the urgency of a task changes.

#### Define boundaries

Once again, the goal is generally to achieve some sort of parallelism between your team members.
In order to do that, they need to know how they will interact with each other.

On a more general level, this means knowing the responsibilities and scope of your work.

On a more specific level, it means knowing their dependency graph.
In other words, whether the progress of one team member will depend on the results of another one.
Whenever there is a dependency, the interface should be made very clear.
This often takes the form of an API, a file with a given format, or a section of a document.

Take some time to define the boundary as precisely as needed at that point in the project.
I would suggest having specific examples that you can discuss and modify.
When in doubt, default to the simplest option (e.g., a common file vs using a database).
Do not dwell too much on specific structural/representation details (e.g., which OWL vocabulary to use), but make sure that all the necessary bits are there.
Converting a document or querying a document store (e.g., elasticsearch) instead of your file system is relatively easy, but making up non-existing data can be a challenge.

#### Be approachable

Did I wrote a whole section about autonomy? Yes.
Is the end goal to do more and talk less? Also yes.
Thing is, no process is perfect, and misunderstandings are bound to happen at some point.
If your only response to questions is a grumpy face or a "read the freaking docs", your students will not alert you when something really needs your attention, and you will find out too late.
For instance, the documentation may be unclear, or your processes may be inadvertedly alienating new members and making new hires harder.

Another way to be approachable is to be clear about your shortcomings, and whether something you are saying is negotiable and/or debatable.
My rule of thumb is to err on the side of negotiable, and only be strict when it is really necessary (e.g., time constraints or an unproductive student).
We are all more likely to finish our tasks if we feel them ours, if we a say in how and when to perform them.

Just to be clear, approachable does not mean you have to be their confident or their best friend.
It also does not mean that it is okay to challenge or question you continuously.
Some times it is okay to simply say "just do as I say".

#### Review frequently

One type of review is individual.
It involves reviewing code on github, or reading deliverables and papers on overleaf.
It can help catch misunderstandings, and measure the true rate of progress in the individual tasks.
The other type of review is done as a group, by going through the key progress and action points.
This type of review helps everyone stay on the same page, and catch any general drifts in the project, such as misaligned priorities.

The frequency of each type of review depends on the specific nature of the project, the types of tasks being performed by the student, and your confidence on the student's abilities.


### Optimizing your contribution

Tips on optimizing your contribution to the team.

#### Prioritize, prioritize, prioritize

Part of your job as a project lead is to identify the main goals in a project and to prioritize the tasks that will lead you there.
On the other hand, you are part of a research group, and you should be actively involved in its health and future.
Lastly, you are also in charge of the life-long project that is your research career.

In all these cases, your goal should be to identify the long term goals, come up with a sound strategy, and prioritize the tasks that will lead you and your group there.
Keeping your priorities straight will help you make steady progress, and avoid bikeshedding and changing goalposts.
It will also help you steer your progress in the right direction, since we all have limited time and effort and can't do everything at once.

The fact that your time is limited also means that you will need to decide how to prioritize these three roles.
I've listed them in increasing level of importance for me.
It means that it is okay to focus on a specific project for a while, but if progress in your career is stalled - usually through publication - you need to reevaluate and concentrate your efforts on that.

#### Be okay with (short-term) inefficiencies 

I've personally struggled with delegating tasks that will take me orders of magnitude less work than they will a student.
Thing is, most tasks will fall under this category, and your time is limited, so you have to delegate if you want to have time for more important matters.
If you never delegate any tasks, you are not allowing your team to learn and catch up on whatever technical skills are required.
Besides, you are not improving yourself on the managerial side of things.
It turns out delegating is hard, it requires a whole set of non-technical skills.
I suspect this is oftentimes the reason we don't do delegate in the first place: delegating is hard, and technical tasks are usually more straightforward, so we just don't want to do the work.

#### Don't neglect training

You are a senior researcher.
You probably know how to solve problems in your domain quite efficiently.
In my case, that means processing data and developing code.

That means I could dedicate my days to processing data and developing new code for my group.
That group would likely be used in multiple projects.
However, there is a hard limit to how much code I can push out in a day, especially if you take into account other obligations such as teaching.

A wiser strategy would be to set aside some of that coding time to instead help students become better programmers.
Firstly, because those students will be thankful and more motivated to work than when they are left to learn on their own without much guidance.
Secondly, because those students will then be more prepared to help me out if I delegate a task to them.
And, lastly, because these students have a whole life in fron of them.
A life full of big projects of their own, and contributions to society.
That little training time can have a compounding effect in the future.


#### Set a time limit for your interactions in advance

Really long slots can easily lead to bikeshedding and going unnecessarily deep into implementation details, which is clearly an inefficient use of your time.
Even worse, our attention span and memory are finite, so longer and dense meetings can lead to fatigue and to missing or dilluting important points in the conversation.

For these reasons, be very clear about these time limits, and do not extend these meetings unless it is strictly necessary.
You can always schedule a new meeting, but be sure to provide enough time in between to process the results of the meeting, reflect and prioritize.
