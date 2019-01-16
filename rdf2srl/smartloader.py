import itertools
import pandas as pd
from pandas import Series
import json

from .queries import *
from .client import Client
from .rdfloader import RDFGraphDataset

__author__ = "Aisha Mohamed <ahmohamed@qf.org.qa>"


class SmartRDFGraphDataset(RDFGraphDataset):
	"""
	A class for loading and processing RDF datasets for relational learning models
	It provides some convenience functions for accessing a knowldge graph from a sparql endpoint
	"""
	def __init__(self, sparql_endpoint, graph_name=None):
		super(SmartRDFGraphDataset, self).__init__(sparql_endpoint, graph_name)

	def entity2entity_triples(self, return_format='list', entity2idx=None, relation2idx=None,
		return_dict = False, output_dir=None):
		"""
		A function that returns all the entity2entity triples in the specified graph as indices rather than URIs
		:param entity2idx: a dictionary mapping each entity in the graph to an index from 0 to n_entities-1
		:param relation2idx: a dictionary mapping each entity in the graph to an index from 0 to n_relations-1
		:param return_format: one of ['list', 'df']
		:return: the triples in the graph in the specified format
		"""
		if entity2idx is None:
			if self.entity2idx is None:
				print("getting entities using self.entities()")
				entity2idx = self.entities('dict')
			else:
				print("entity2idx = self.entity2idx")
				entity2idx = self.entity2idx
		#print(len(entity2idx))
		# find the dictionary mapping each relation to its index
		if relation2idx is None:
			if self.relation2idx is None:
				print("getting relations using self.relations()")
				relation2idx = self.relations('dict')
			else:
				print("relation2idx = self.relation2idx")
				relation2idx = self.relation2idx

		#print('relation2idx = \n{}'.format(relation2idx))

		results_df = pd.DataFrame(columns=['subject', 'object', 'predicate'])
		for relation in relation2idx:
			query_string = str(PTriples(self.graph, relation))
			#print("query string is \n{}".format(query_string))
			result_df = self.client.execute_query(query_string)
			#print(result_df.head())
			#print(result_df.shape)
			result_df.columns = ['subject', 'object', 'predicate']
			result_df['subject'] = result_df['subject'].map(entity2idx)
			result_df['object'] = result_df['object'].map(entity2idx)
			result_df['predicate'] = result_df['predicate'].map(relation2idx)
			#print(result_df.head())
			results_df = pd.merge(results_df, result_df, how='outer')
			#results_df = pd.concat([results_df, result_df], ignore_index=True)
			#print(results_df.shape)
		
		if output_dir is not None:
			results_df.to_csv(output_dir+"/entity2entity_triples.csv")
			with open(output_dir+"/relation2idx.json", 'w') as fp:
				json.dump(relation2idx, fp)
			with open(output_dir+"/entity2idx.json", 'w') as fp:
				json.dump(entity2idx, fp)

		if return_format == 'list':
			if return_dict:
				return results_df.values.tolist(), entity2idx, relation2idx
			return results_df.values.tolist() 
		elif return_format == 'df':
			if return_dict:
				return results_df, entity2idx, relation2idx
			return results_df


	def entity2literal_triples(self, entity2idx=None, attribute_literal_pair2idx=None, return_format='list'):
		"""
		A function that returns all the entity2literal triples in the specified graph as indices rather than URIs
		:param entity2idx: a dictionary mapping each entity in the graph to an index from 0 to n_entities-1
		:param attribute_literal_pair2idx: a dictionary mapping each entity in the graph to an index from 0 to
		n_relations-1
		:param return_format: one of ['list', 'df']
		:return: the triples in the graph in the specified format
		"""
		query_string = str(E2LTriples(self.graph))
		result_df = self.client.execute_query(query_string)
		# find the dictionary mapping each entity to its index
		if entity2idx is None:
			if self.entity2idx is None:
				entity2idx = self.entities('dict')
			else:
				entity2idx = self.entity2idx
		# find the dictionary mapping each predicate,literal pair to its index
		if attribute_literal_pair2idx is None:
			if self.attribute_literal_pair2idx is None:
				attribute_literal_pair2idx = self.attr_literal_pairs('dict')
			else:
				attribute_literal_pair2idx = self.attribute_literal_pair2idx

		result_df.columns = ['subject', 'predicate', 'object']
		result_df['attribute_literal_pair'] = result_df[['predicate', 'object']].apply(lambda x: ','.join(str(x)), axis=1)

		# map the subjects to their indices
		result_df = result_df.replace({'subject': entity2idx})
		result_df = result_df.replace({'attribute_literal_pair': attribute_literal_pair2idx})

		if return_format == 'list':
			return result_df.values.tolist()
		elif return_format == 'df':
			return result_df


	def subjects(self, p, entity2idx=None, return_format='list'):
		"""
		A function that returns all the subjects of predicate p in the specified graph as indices rather than URIs
		:param entity2idx: a dictionary mapping each entity in the graph to an index from 0 to n_entities-1
		:param return_format: one of ['list', 'df']
		:return: the triples in the graph in the specified format
		"""
		query_string = str(Subjects(self.graph, p))
		result_df = self.client.execute_query(query_string)
		# find the dictionary mapping each entity to its index
		if entity2idx is None:
			if self.entity2idx is None:
				entity2idx = self.entities('dict')
			else:
				entity2idx = self.entity2idx

		result_df.columns = ['subject']
		# map the subjects to their indices
		result_df['subject'] = result_df['subject'].map(entity2idx)

		if return_format == 'list':
			return result_df.values.tolist()
		elif return_format == 'df':
			return result_df

	def objects(self, p, entity2idx=None, return_format='list'):
		"""
		A function that returns all the objects of predicate p in the specified graph as indices rather than URIs
		:param entity2idx: a dictionary mapping each entity in the graph to an index from 0 to n_entities-1
		:param return_format: one of ['list', 'df']
		:return: the triples in the graph in the specified format
		"""
		query_string = str(Objects(self.graph, p))
		result_df = self.client.execute_query(query_string)
		# find the dictionary mapping each entity to its index
		if entity2idx is None:
			if self.entity2idx is None:
				entity2idx = self.entities('dict')
			else:
				entity2idx = self.entity2idx

		result_df.columns = ['object']
		# map the subjects to their indices
		result_df['object'] = result_df['object'].map(entity2idx)

		if return_format == 'list':
			return result_df.values.tolist()
		elif return_format == 'df':
			return result_df