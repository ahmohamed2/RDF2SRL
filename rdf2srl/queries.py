__author__ = "Aisha Mohamed <ahmohamed@qf.org.qa>"


class SparqlQuery(object):
	"""
	A class for the sparql query
	"""
	def __init__(self, graph):
		super(SparqlQuery, self).__init__()
		self.graph = graph

	def __str__(self):
		pass


class NTriples(SparqlQuery):
	"""
	A class for the sparql query that returns the number of triples
	"""

	def __str__(self):
		return 'SELECT count(*) FROM <' + self.graph + '> WHERE { ?s ?p ?o}'


class NE2ETriples(SparqlQuery):
	"""
	A class for the sparql query that returns the number of triples
	"""

	def __str__(self):
		return 'PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT count(*) FROM <' + self.graph + \
			'> WHERE {?s ?p ?o {SELECT DISTINCT ?p WHERE { ?s ?p ?o . ?o rdf:type ?c}}}'


class NE2LTriples(SparqlQuery):
	"""
	A class for the sparql query that returns the number of triples
	"""

	def __str__(self):
		return 'SELECT count(*) FROM <' + self.graph + '> WHERE { ?s ?p ?o . {SELECT DISTINCT ?p FROM <' + \
			self.graph + '> WHERE { ?s ?p ?o . FILTER isLiteral(?o)}}}'

class NEntities(SparqlQuery):
	"""
	A class for the sparql query that returns the number of entities
	"""
	def __str__(self):
		return 'PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT count(DISTINCT ?s) FROM <' \
			+ self.graph + '> WHERE {?s rdf:type ?c}'


class NPredicates(SparqlQuery):
	def __str__(self):
		return 'SELECT COUNT(DISTINCT ?p) FROM <' + self.graph + '> WHERE { ?s ?p ?o }'


class NRelations(SparqlQuery):
	"""
	A class for the sparql query that returns the number of relations
	"""
	def __str__(self):
		return 'PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT count(DISTINCT ?p) FROM <' + \
			self.graph + '> WHERE { ?s ?p ?o . ?o rdf:type ?c}'


class NAttributes(SparqlQuery):
	"""
	A class for the sparql query that returns the number of attributes
	"""
	def __str__(self):
		return 'SELECT count(DISTINCT ?p) FROM <' + self.graph + '> WHERE { ?s ?p ?o . FILTER isLiteral(?o)}'


class NAttributeLiteralPairs(SparqlQuery):
	"""
	A class for the sparql query that returns the number of attr_literal_pairs
	"""
	def __str__(self):
		return 'SELECT COUNT (*) WHERE {SELECT DISTINCT ?p ?o FROM <' + self.graph + \
			'> WHERE { ?s ?p ?o . FILTER isLiteral(?o)}}'


class Triples(SparqlQuery):
	"""
	A class for the sparql query that returns the triples
	"""
	def __str__(self):
		return 'SELECT count(*) FROM <' + self.graph + '> WHERE { ?s ?p ?o}'


class E2ETriples(SparqlQuery):
	"""
	A class for the sparql query that returns the number of triples
	"""

	def __str__(self):
		return 'PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT * FROM <' + self.graph + \
			'> WHERE {?s ?p ?o {SELECT DISTINCT ?p WHERE { ?s ?p ?o . ?o rdf:type ?c}}}'


class E2LTriples(SparqlQuery):
	"""
	A class for the sparql query that returns the number of triples
	"""

	def __str__(self):
		return 'SELECT * FROM <' + self.graph + '> WHERE { ?s ?p ?o . {SELECT DISTINCT ?p' + \
			'WHERE { ?s ?p ?o . FILTER isLiteral(?o)}}}'


class Entities(SparqlQuery):
	"""
	A class for the sparql query that returns the entities
	"""
	def __str__(self):
		return 'PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?s FROM <' + \
			self.graph + '> WHERE {?s rdf:type ?c}'


class Relations(SparqlQuery):
	"""
	A class for the sparql query that returns the entity to entiity relations
	"""
	def __str__(self):
		return 'PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> SELECT DISTINCT ?p FROM <' + \
			self.graph + '> WHERE { ?s ?p ?o . ?o rdf:type ?c}'


class Attributes(SparqlQuery):
	"""
	A class for the sparql query that returns the  attributes
	"""
	def __str__(self):
		return 'SELECT DISTINCT ?p FROM <' + self.graph + '> WHERE { ?s ?p ?o . FILTER isLiteral(?o)}'


class Predicates(SparqlQuery):
	"""
	A class for the sparql query that returns the predicates
	"""
	def __str__(self):
		return 'SELECT DISTINCT ?p FROM <' + self.graph + '> WHERE { ?s ?p ?o }'


class AttributeLiteralPairs(SparqlQuery):
	"""
	A class for the sparql query that returns the attr_literal_pairs
	"""
	def __str__(self):
		return 'SELECT DISTINCT ?p ?o FROM <' + self.graph + '> WHERE { ?s ?p ?o . FILTER isLiteral(?o)}'


class Subjects(SparqlQuery):
	"""
	A class for the sparql query that returns the subjects of a given predicate p.
	It returns all the subjects ?s that match the following pattern
		?s p ?o
	"""
	def __init__(self, graph, p):
		super(SparqlQuery, self).__init__(graph)
		self.p = p

	def __str__(self):
		return 'SELECT DISTINCT ?s FROM <' + self.graph + '> WHERE { ?s ' + self.p + ' ?o }'


class Objects(SparqlQuery):
	"""
	A class for the sparql query that returns the objects of a given predicate p.
	It returns all the objects ?o that match the following pattern
		?s p ?o
	"""
	def __init__(self, graph, p):
		super(SparqlQuery, self).__init__(graph)
		self.p = p

	def __str__(self):
		return 'SELECT DISTINCT ?p FROM <' + self.graph + '> WHERE { ?s ' + self.p + ' ?o }'


class PredicatesFreq(SparqlQuery):
	"""
	A class for the sparql query that returns the predicates of a given graph.
	It returns all the predicates ?p that match the following pattern
		?s p ?o
	"""
	def __str__(self):
		return 'SELECT COUNT(DISTINCT *) FROM <' + self.graph + '> WHERE { ?s ?p ?o } GROUPBY ?p'
