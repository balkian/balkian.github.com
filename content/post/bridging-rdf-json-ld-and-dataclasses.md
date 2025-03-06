---
title: "Bridging RDF, JSON-LD and Dataclasses"
description: 
date: 2025-02-26T23:22:59+01:00
image: 
math: 
license: 
hidden: false
comments: true
draft: false
categories:
    - programming
tags:
    - rdf
    - json-ld
    - pydantic
    - python
---

In the RDF world, data is expressed as a collection of triples.
These triples can contain IRIs that may or may not be accessible or valid.
And the use of these IRIs may or may not adhere to a vocabulary.
Checking the validity of the IRIs and the semantics of the triples is an additional step.

## The `rdflib` way
 
`rdflib` only models IRIs, values and namespaces.
Developers need to be cognisant of the URIs they are using, and the vocabularies being used.
Prior to version 2.0, senpy followed a very similar model.
It had a base class to represent a generic node.
Each instance then gets its own automatically generated id, and will act like a normal dictionary, whose keys and values will be serialized as a JSON-LD dictionary.
Multiple subclasses were also included to model specific types of node, mostly to provide convenience methods for the given subtype.
Here is an example of a subclass, `Entity`.

```python
entry = Entry()

entry['vocab:property'] = 25

print(entry.jsonld())
```

Would print something like this:

```json
{
 "@id": ":Entry_202505....",
 "@type": "prefix:Entity",
 "vocab:property": 25
}
```

Producing correct triples using this model requires using the vocabularies and URIs properly, with little to no tooling to enforce it.
This poses a big problem for a tool like Senpy, which aims to make it easier for professionals without a background in RDF to build and consume semantic NLP ser
If an attribute is not a URI and is not included in the global JSON-LD context, it will not generate a triple in the final graph.
Moreover, there is way to enforce that the vocabularies and the 

Pros:
* Flexible/extensible
* Lightweight. This is mostly JSON-LD in Python's clothing.
* Naturally maps to both `rdflib` and writing `json-ld`

Cons:
* Discoverability. Documentation and examples are needed to know which attributes to use
* Error-prone. It is easy to misuse a property, or introduce typos
* Tight coupling with semantics/RDF. One needs to know a thing or two about RDF, especially if new vocabularies or annotations need to be used.

## The object-oriented way
 
An obvious alternative to this problem in an object-oriented language like python is to use classes to represent our data model.
These classes can define the specific attributes available, and typing annotations can serve both as a guide for the developer, and as a means to automatically 
validate objects at runtime.
There are tools like [pydantic](https://pydantic.dev/) that make this process very simple.
Then, we only need to define how your models should be serialized into JSON-LD.
We can thoroughly test this serialization to ensure that the resulting object is correct and produces the right RDF graph.
Going back to our previous example, we could define an Entry class as a dataclass, and define all the possible types of annotations as attributes.

This model works great when all the possible attributes are known ahead of time.
But it starts to break when the model provided is not comprehensive enough, or customers of your library need to provide their own ad-hoc annotations / attribut
es.
This could be solved by encouring consumers of our library to define their own subclasses whenever they need to add new attributes.
This works perfectly fine for serialization, but it breaks if your library needs to automatically deserialize these subclasses.
It also breaks if different parts of the code need to add their own attributes on the same data at the same time.
This was precisely the case of `senpy`, where entities are annotated by different plugins, each providing a different set of annotations.

Pros:
* Discoverability. All possible attributes are known ahead of time, including their possible types.
* Decoupling from RDF. Developers only need to know about the dataclasses provided. The mapping to the RDF world is already encoded in the dataclass.

Cons:
* Rigidity. Adding new types of annotations requires modifying the models, in the main module.
* Polymorphism. 
                                                                                     
                                                                                                          
## A hybrid approach

Whichever solution is chosen in the end, it needs to:                                                                 
                                                                                                                      
* Make it easy and error-proof to add the most common types of annotations                                            
* Allow for additional annotations/attributes to be added                                                             
* Allow for upgrades in the future. i.e., converting the most common custom annotations into built-in ones            
* Allow for deserialization of custom types                                                               
* Allow multiple consumers to add their own annotations

