# RDF2SRL

This package exposes RDF data from sparql database engines for relational 
learning models.

It provides some convenience functions that send sparql queries in http 
requests for both open ans private sparql endpoint. 

## Getting Started
We can use this package to get some statistics about the DBpedia dataset.
Let's use the [DBpedia public endpoint](http://dbpedia.org/sparql) provided 
by [OpenLink Virtuoso](http://dbpedia.org/page/Virtuoso_Universal_Server)

First, import the ```RDFGraphDataset``` class from the python package ```rdf2srl```
```python
from rdf2srl import RDFGraphDataset
```
Second,
initialize the ```RDFGraphDataset``` class with the endpoint uri and the graph uri
```python
    loader = RDFGraphDataset(sparql_endpoint="http://dbpedia.org/sparql", graph_name='http://dbpedia.org/')
```
Now, Let's find the number of (subject, predicate, object) triple in the DBpedia graph:
```python
num_triples = loader.num_triples()
```
To find the number of (subject, predicate, object) triples where the object is another entity,
find the number of entity to entity triples.
```python
num_e2e_triples = loader.num_entity2entity_triples()
```
To find the number of (subject, predicate, object) triples where the object is a literal value,
find the number of entity to entity triples.
```python
num_e2l_triples = loader.num_entity2literal_triples()
```

We can also use the package to access the entities in the graph. A useful format for
relational learning is a dictionary that maps each entity to an index that starts
from 0 to n_entities-1.
```python
entity2idx = loader.entities('dict')
```

the triples in the dataset as list of tuples
where the values inside triples represent the 

