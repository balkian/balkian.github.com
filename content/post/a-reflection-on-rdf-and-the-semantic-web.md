---
title: "A Reflection on RDF and the Semantic Web"
description: 
date: 2025-03-04T19:19:53+01:00
image: 
math: 
license: 
hidden: false
comments: true
draft: true
---

I've been involved with semantic technologies almost for as long as I've been building software.
Before my internship at the Intelligent Systems Group in 2009, I had done very little programming.
This more or less coincidences with the rise of the semantic web.
Given GSI's background with knowledge representation and web engineering, it should be no surprise that many projects back then involved RDF and semantic technologies.
Moreover, most of the projects since then have been related to semantic technologies in some shape or form.

I remember being intrigued, then fascinated, with the idea of linked data.
Representing knowledge in a way that allows both humans and machines to consume it seemed so obvious.
In a way, it also tickled my "distributed systems" bone, with the whole "distributed and collaborative graph of knowledge".
But it would not really get involved with the semantic web until years later, as part of my PhD thesis.

First, I was tasked with extending an existing vocabulary for sentiment analysis ([Marl](https://www.gsi.upm.es/ontologies/marl/)) to include provenance information (Prov-O).
Then I applied the same ideas to define a new vocabulary for emotion analysis ([Onyx](https://www.gsi.upm.es/ontologies/onyx)).

Not long after that, I started working on a framework to allow laypeople to develop "semantic NLP services".
It was already apparent to me that developing proper semantic services was out of reach (or interest) for the average programmer.
There were too many concepts to learn (vocabularies, RDF-XML, turtle, inference...) without much push from industry to learn them.
But I was still convinced that a semantic framework would lead to interoperability and flexibility.
And those two benefits would lead to more adoption, ease of use, and more useful applications being developed.
Besides, I was less focused on the long term viability of the project and more interested in the technical and usability challenges.

Building that framework has taught me very valuable lessons, which I'll probably get into in a separate post.
On the topic of RDF and the semantic web, it made me deal with the reality of developing real semantic services that other consumers depend on, witnessing undergrads struggle with semantic annotations while developing their own services for their thesis, and building data annotation pipelines that rely on said services and their made-up annotations.

## The good

### Unique identifiers allow for federated knowledge graphs

### RDF's data model is neat

Modelling every fact as a triple is very powerful.
Moreover, it makes it possible to represent your schema/vocabularies using the same raw elements.
At the same time, it can be confusing for newcomers to grasp the difference between a vocabulary (TBox) and the data graph (ABox).

### SPARQL is quite versatile

### Linking data should provide a network effect

## The bad

### Defining vocabularies is tricky

### Vocabularies are not properly maintain

### Projects in the semantic space are not properly maintained


## The ugly

### Nobody cares about it
