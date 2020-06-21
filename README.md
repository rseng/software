# Research Software

[**annotate**](https://rseng.github.io/rse/tutorials/annotation/) this research software.

What is research software? Simply stated, research software exists to support
research. If we want to pursue better research, we then must understand it [3].
This leads us to ask some basic question:

 1. What is research software
 2. What are criteria that might help to identify research software?
 3. How do we organize research software?

While we could make an attempt to derive a holistic definition, this approach 
would be limited in not taking into account the context under which the definition
is considered. For example, needing to define research software to determine
eligibility for a grant is a different scenario than a journal needing
to decide if a piece of software is in scope for publication, and both
are different from an effort to study research software. In all cases, 
the fundamental need for a context-specific definition is not only important in these
scenarios, but also for basic communication. If I am to call something research
software, it's essential that you know the criteria that I am using to consider it,
how highly I consider each of those criteria, and a possibly classification
that I am using to further drive my choices.

## A Context Specific Definition

This repository, paired with [the document that prompted its original thinking](https://docs.google.com/document/d/1wDb0udH9OrFWrMBsAVb8RrUMCKKRHoyEep7yveJ1d0k/edit), takes the stance that it would be
very challenging if not possible to create a single definition for research software.
However, it's very reasonable to derive criteria, or questions that we can easily
answer, that can be used to determine a relative strength of a piece of software
on a dimension of "strongly yes" to "strongly no." We can also derive a taxonomy,
or categorization of research software types that might further filter this decision
making. Both of these classifications, a scoring and location in the taxonomy,
can then be transparently stated and used to answer if a specific piece of software
is indeed research software. Importantly, while the choice of threshold for scoring
and taxonomy filter is subjective, the classification and answers to the criteria
are not. We have a transparent, methodic way to define pieces of software, and we leave
some final definition up to the individual or group that warrants needing the definition.

## Understanding for Science

An understanding of the qualities of software that are required to support 
this research life-cycle is essential to continue and maximize the potential for discovery. 
In this light, research software is also about people, namely the developers and 
community that utilizes it. If we can better characterize this community to 
better understand how its needs map to research software, we can again better support scientific discovery.

[3] C. Goble, "Better Software, Better Research," in IEEE Internet Computing, vol. 18, no. 5, pp. 4-8, Sept.-Oct. 2014, doi: 10.1109/MIC.2014.88.


# Development Work

## Database

Using the [rseng/rse](https://github.com/rseng/rse) library we can run an automated nightly
job to update our software database, located under [database](database) and represented
with the configuraiton file [rse.ini](rse.ini). This nightly job will also automatically
update an interface that deploys a static API for it (under development).

## Taxonomy and Criteria

The taxonomy, list of software, and criteria should be developed at the same time,
and open to community contribution. The original lists are [derived from the original document](https://docs.google.com/document/d/1wDb0udH9OrFWrMBsAVb8RrUMCKKRHoyEep7yveJ1d0k/edit) and represented here.

 - [software](software) database development.
 - [taxonomy](taxonomy) development.
 
Separate software will be developed for interacting with these entities.

## Taxonomy Development

Before creating a programmatic representation of a taxonomy, we might develop categories
based on a thought experiment of attempting to classify a set of well known software libraries.
In fact, 
