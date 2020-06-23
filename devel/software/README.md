## Software Database

This will be a namespaced flat database of research software. Each namespace must have
a programmatic API to retrieve updated metadata about the software, and within
the namespace, unique identifiers (e.g., GitHub has an API and identifiers that
correspond to the repository name). You don't have to agree that all software here
is research software - the idea is to have a flat database that we can render
into an interface and answer questions about it's grouping (taxonomy) and
features (criteria).

Top level namespaces include:

 - [github.com](github.com)


**under development**

## Development

I had an idea is to start with the scicrunch (rrid) resources, and narrow down to:

 - tools
 - software applications
 - open source or openly available

A search represnted by [this query](https://scicrunch.org/resources/Tools/search?q=%2A&l=&facet[]=Resource%20Type%3Asoftware%20application&sort=asc&column=Proper%20Citation&sort=asc&facet[]=Availability:Free&facet[]=Availability:Available%20for%20download&facet[]=Availability:Freely%20available&facet[]=Availability:GNU%20General%20Public%20License&facet[]=Availability:Open%20source&facet[]=Availability:Public&facet[]=Availability:BSD%20License) 
done on May 31st that resulted in 1,668 results. I started attempting to use the scicruch API using [get_software_scicrunch.py](get_software_scicrunch.py) but wasn't able to figure out
the usage, and some endpoints were returning errors. Instead I created a simple
method to submit software (that could easily be from this database)

[**submit**](https://forms.gle/P8kx8o994FhRBuCXA) research software


## TODO:

 - create GitHub root for GitHub repos, and script to parse metadata for them
 - create simple module that can do the same?
 - create JoSS script to find new GitHub repos
 - maybe something with zenodo?
