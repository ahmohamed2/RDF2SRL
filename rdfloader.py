from queries import *
from client import Client

__author__ = "Aisha Mohamed <ahmohamed@qf.org.qa>"


class RDFGraphLoader(object):
	"""
	A class for loading and processing RDF datasets for
	relational learning models
	It provides some convenience functions for accessing a knowldge graph from a sparql endpoint
	"""

	def __init__(self, sparql_endpoint, graph_name):
		super(RDFLoader, self).__init__()
		self.graph = graph_name
		self.endpoint = sparql_endpoint
		self.client = Client(self.endpoint)
		self.entity2idx = None
		self.relation2idx = None
		self.attribute2idx = None

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

	def entities(self, return_format='dict'):
		"""
		A function that returns the number of
		:param return_format: the return format of the result. one of ['dict', 'df', 'list']
		:return: the entities in the knowledge graph represented in the specified return format
		"""
		query_string = str(Entities(self.graph))
		result_df = self.client.execute_query(query_string)
		if return_format == 'dict':
			# TODO: set the index to the entities column
			idx2entity_dict = result_df.set_index('').T.to_dict('list')
			return idx2entity_dict
		elif return_format == 'df':
			return result_df
		elif return_format == 'list':
			# TODO: implement the list format
			pass

	def triples(self, entity2idx=None):
		query_string = str(Entities(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the triples of URIs to triples of indices
		return result

	def relations(self):
		query_string = str(Relations(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the dataframe to an indexed dictionary
		return result

	def attributes(self):
		query_string = str(Attributes(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the dataframe to an indexed dictionary
		return result

	def attr_literal_pairs(self):
		query_string = str(AttributeLiteralPairs(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the dataframe to an indexed dictionary
		return result

	def subjects(self, p):
		pass

	def objects(self, p):
		pass








