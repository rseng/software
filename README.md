# Research Software

 - [**annotate**](https://rseng.github.io/software/) a repository in the static web interface or by [opening an issue](https://github.com/rseng/software/issues/new/choose) or in bulk [on your local machine](https://rseng.github.io/rse/tutorials/annotation/) 
 - [**view**](https://rseng.github.io/software/) this research software, taxonomy, and criteria
 - Use the **api** to see [repos](https://rseng.github.io/software/api/repos/index.json), [taxonomy](https://rseng.github.io/software/api/taxonomy/index.json), and [criteria](https://rseng.github.io/software/api/criteria/index.json)

**coming soon** annotate statically on the GitHub pages here, and automated weekly annotation prompts on social media and slack.

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

## How does it work?

 1. **Taxonomy and Criteria** are served programaticaly from the [Research Software Engineering (rseng)](https://rseng.github.io/rseng) repository. If you want to contribute to either of those, that's the repository you should contribute to.
 2. **Database**: the [Research Software Encyclopedia](https://github.com/rseng/rse) drives generation and update of the database here.
 3. **Update** is automated using [GitHub Workflows](.github/workflows) that are run on a weekly bases.
 4. **Annotate** via the command line or web interface by cloning the repository to and following instructions in the [annotate docs](https://rseng.github.io/rse/tutorials/annotation/). Your contribution is recorded in the git history, and your avatar is added to the contributor graphic. Other methods of annotation will also be available.

## Web Interface

A static web interface of the software database is generated automatically and served
by the repository at [https://rseng.github.io/software/](https://rseng.github.io/software/). If you want to generate this
manually you can do:

```bash
rse export --type static-web docs/
rse export --type static-web docs/ --force # if exists
```

Further, a static API is exported to [https://rseng.github.io/software/data.json](https://rseng.github.io/software/data.json) that provides a listing of your software repositories
for some programmatic usage.

# Development Work

For previous development work, see the [devel](devel) folder.
