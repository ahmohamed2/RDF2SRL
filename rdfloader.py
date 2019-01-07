from pandas import Series
import itertools

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
		super(RDFGraphLoader, self).__init__()
		self.graph = graph_name
		self.endpoint = sparql_endpoint
		self.client = Client(self.endpoint)
		self.entity2idx = None
		self.predicate2idx = None
		self.relation2idx = None
		self.attribute2idx = None

	def num_entities(self):
		"""
		:return: integer representing the number of entities
		"""
		query_string = str(NEntities(self.graph))
		result = self.client.execute_query(query_string)
		result = result.values.tolist()[0][0]
		return result

	def num_predicates(self):
		"""
		:return: integer representing the number of relations
		"""
		query_string = str(NPredicates(self.graph))
		result = self.client.execute_query(query_string)
		result = result.values.tolist()[0][0]
		return result

	def num_relations(self):
		"""
		:return: integer representing the number of relations
		"""
		query_string = str(NRelations(self.graph))
		result = self.client.execute_query(query_string)
		result = result.values.tolist()[0][0]
		return result

	def num_attributes(self):
		"""
		:return: integer representing the number of attributes
		"""
		query_string = str(NAttributes(self.graph))
		result = self.client.execute_query(query_string)
		result = result.values.tolist()[0][0]
		return result

	def num_attr_literal_pairs(self):
		"""
		:return: integer representing the number of attribute literal pairs
		"""
		query_string = str(NAttributeLiteralPairs(self.graph))
		result = self.client.execute_query(query_string)
		result = result.values.tolist()[0][0]
		return result

	def num_triples(self):
		"""
		:return: integer representing the number of triples
		"""
		query_string = str(NTriples(self.graph))
		result = self.client.execute_query(query_string)
		result = result.values.tolist()[0][0]
		return result

	def num_entity2entity_triples(self, entity2idx=None):
		"""
		:return: integer representing the number of entity to entity triples
		"""
		query_string = str(NE2ETriples(self.graph))
		result = self.client.execute_query(query_string)
		result = result.values.tolist()[0][0]
		return result

	def num_entity2literal_triples(self, entity2idx=None):
		"""
		:return: integer representing the number of entity to literal triples
		"""
		query_string = str(NE2LTriples(self.graph))
		result = self.client.execute_query(query_string)
		result = result.values.tolist()[0][0]
		return result

	def entities(self, return_format='dict'):
		"""
		A function that returns the entities in the graph
		:param return_format: one of ['dict', 'df', 'list']
		:return: the entities in the knowledge graph represented in the specified return format
		"""
		query_string = str(Entities(self.graph))
		result_df = self.client.execute_query(query_string)

	def predicates(self, return_format='dict'):
		query_string = str(Predicates(self.graph))
		result_df = self.client.execute_query(query_string)
		# set the column name to "relation"
		result_df.columns = ['predicate']
		# create a new column for the index
		result_df.reset_index(level=0, inplace=True)
		# convert it to a dictionary and store it
		predicate2idx = Series(result_df['index'].values, index=result_df['predicate'].values).to_dict()
		self.predicate2idx = predicate2idx

		if return_format == 'dict':
			return predicate2idx
		elif return_format == 'df':
			return result_df
		elif return_format == 'list':
			return list(itertools.chain(*result_df.values))		

	def relations(self, return_format='dict'):
		"""
		A function that returns the relations in the graph
		:param return_format: one of ['dict', 'df', 'list']
		:return: the entities in the knowledge graph represented in the specified return format		
		"""
		query_string = str(Relations(self.graph))
		result_df = self.client.execute_query(query_string)
		# set the column name to "relation"
		result_df.columns = ['relation']
		# create a new column for the index
		result_df.reset_index(level=0, inplace=True)
		relation2idx = Series(result_df['index'].values, index=result_df['relation'].values).to_dict()

		if return_format == 'dict':
			return relation2idx
		elif return_format == 'df':
			return result_df
		elif return_format == 'list':
			return list(itertools.chain(*result_df.values))

	def attributes(self, return_format='dict'):
		"""
		A function that returns the attributes in the graph
		:param return_format: one of ['dict', 'df', 'list']
		:return: the attributes in the knowledge graph represented in the specified return format		
		"""
		query_string = str(Attributes(self.graph))
		result_df = self.client.execute_query(query_string)
		# set the column name to "relation"
		result_df.columns = ['attribute']
		# create a new column for the index
		result_df.reset_index(level=0, inplace=True)
		attribute2idx = Series(result_df['index'].values, index=result_df['attribute'].values).to_dict()
		self.attribute2idx = attribute2idx

		if return_format == 'dict':
			return attribute2idx
		elif return_format == 'df':
			return result_df
		elif return_format == 'list':
			return list(itertools.chain(*result_df.values))

	def attr_literal_pairs(self, return_format='dict'):
		"""
		A function that returns the attributes in the graph
		:param return_format: one of ['dict', 'df', 'list']
		:return: the attributes in the knowledge graph represented in the specified return format		
		"""
		query_string = str(AttributeLiteralPairs(self.graph))
		result = self.client.execute_query(query_string)
		if return_format == 'dict':
			# set the column name to "relation"
			result_df.columns = ['attr_literal_pair']
			# create a new column for the index
			result_df.reset_index(level=0, inplace=True)
			attr_literal_pair2idx = Series(result_df['index'].values, index=result_df['attr_literal_pair'].values).to_dict()
			return attr_literal_pair2idx
		elif return_format == 'df':
			return result_df
		elif return_format == 'list':
			return list(itertools.chain(*result_df.values))

	def triples(self, entity2idx=None):
		query_string = str(Entities(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the triples of URIs to triples of indices
		return result

	def entity2entity_triples(self, entity2idx=None):
		query_string = str(Entities(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the triples of URIs to triples of indices
		return result

	def entity2literal_triples(self, entity2idx=None):
		query_string = str(Entities(self.graph))
		result = self.client.execute_query(query_string)
		# TODO: convert the triples of URIs to triples of indices
		return result


	def subjects(self, p, entity2idx=None):
		query_string = str(Subjects(self.graph, p))
		result = self.client.execute_query(query_string)

	def objects(self, p, entity2idx=None):
		query_string = str(Objects(self.graph, p))
		result = self.client.execute_query(query_string)








