from queries import *
from client import Client

__author__ = "Aisha Mohamed <ahmohamed@qf.org.qa>"


class RDFLoader(object):
	"""
	A class for loading and processing RDF datasets for
	relational learning models
	"""

	def __init__(self, sparql_endpoint, graph_name):
		super(RDFLoader, self).__init__()
		self.graph = graph_name
		self.endpoint = sparql_endpoint
		self.client = Client(self.endpoint)

	def num_entities(self):
		"""
		:return: integer representing the number of entities
		"""
		query_string = str(NEntities(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the dataframe to integer
		return result

	def num_triples(self):
		"""
		:return: integer representing the number of triples
		"""
		query_string = str(NTriples(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the dataframe to integer
		return result

	def num_relations(self):
		"""
		:return: integer representing the number of relations
		"""
		query_string = str(NRelations(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the dataframe to integer
		return result

	def num_attributes(self):
		"""
		:return: integer representing the number of attributes
		"""
		query_string = str(NAttributes(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the dataframe to integer
		return result

	def num_attr_literal_pairs(self):
		"""
		:return: integer representing the number of attribute literal pairs
		"""
		query_string = str(NAttributeLiteralPairs(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the dataframe to integer
		return result

	def entities(self):
		query_string = str(Entities(self.graph))
		result = self.client.execute_query(query_string)
		return result

	def triples(self):
		query_string = str(Entities(self.graph))
		result = self.client.execute_query(query_string)
		return result

	def relations(self):
		query_string = str(Relations(self.graph))
		result = self.client.execute_query(query_string)
		return result

	def attributes(self):
		query_string = str(Attributes(self.graph))
		result = self.client.execute_query(query_string)
		return result

	def attr_literal_pairs(self):
		query_string = str(AttributeLiteralPairs(self.graph))
		result = self.client.execute_query(query_string)
		return result

	def subjects(self, p):
		pass

	def objects(self, p):
		pass








