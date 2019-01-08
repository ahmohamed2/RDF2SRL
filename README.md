# RDF2SRL

This package exposes RDF data from sparql database engines for relational 
learning models.

It provides some convenience functions that send sparql queries in http 
requests for both public and private sparql endpoints. 

## Getting Started
We can use this package to get some statistics about the DBpedia dataset.
Let's use the [DBpedia public endpoint](http://dbpedia.org/sparql) provided 
by [OpenLink Virtuoso](http://dbpedia.org/page/Virtuoso_Universal_Server)

First, import the ```RDFGraphDataset``` class from the python package ```rdf2srl```
```python
from rdf2srl import RDFGraphDataset
```
Second,
initialize the ```RDFGraphDataset``` class with the endpoint URI and the graph URI
```python
    loader = RDFGraphDataset(sparql_endpoint="http://dbpedia.org/sparql", graph_name='http://dbpedia.org/')
```
Now, Let's find the number of (subject, predicate, object) triples in the DBpedia graph:
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
Similarly, we can get all the entity-to-entity predicates in the graph. A useful format for
relational learning is a dictionary that maps each predicate to an index that starts
from 0 to n_relations-1.
```python
relation2idx = loader.relations('dict')
```
Now, we can get the triples in the dataset as list of tuples where the values inside triples represent the
indices in ```entity2idx``` and ```relation2idx```
```python
triples = loader.triples('list')
```

