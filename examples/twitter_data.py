import sys
sys.path.append('/home/amohamed/RDF2SRL/')
from rdf2srl.rdfloader import RDFGraphDataset

loader = RDFGraphDataset(sparql_endpoint="http://192.168.10.2:8890/sparql", graph_name='http://twitter.com/')

#m = loader.num_triples() # 49,216,628
#print("m = {}".format(m))
#n_e = loader.num_entities() # 5,250,147
#print("n_e = {}".format(n_e))
#n_p = loader.num_predicates() # 30
#print("n_p = {}".format(n_p))
#n_r = loader.num_relations() # 10
#print("n_r = {}".format(n_r))
#n_a = loader.num_attributes() # 20
#print("n_a = {}".format(n_a))
#n_al = loader.num_attr_literal_pairs() # 14,449,483
#print("n_al = {}".format(n_al))

#print("n_e = {}  n_p = {}  n_r = {}  n_a = {}  n_al = {}  m = {}".format(n_e, n_p, n_r, n_a, n_al, m))

#e2l_m = loader.num_entity2literal_triples() # 32,427,451
#print("num_entity2literal_triples = {}".format(e2l_m))
#e2e_m = loader.num_entity2entity_triples()
#print("num_entity2entity_triples = {}".format(e2e_m))
#print("m = {}  e2l_m+e2e_m = {}".format(m, e2l_m+e2e_m))


#predicates_dict = loader.predicates('dict')
#print("predicates_dict = \n{}".format(predicates_dict))
#predicates_df = loader.predicates('df')
#predicates_list = loader.predicates('list')
#print("predicates_df = \n{}".format(predicates_df))
#print("predicates_list = \n{}".format(predicates_list))

#relations_dict = loader.relations('dict')
#relations_df = loader.relations('df')
#relations_list = loader.relations('list')
#print("relations_dict = \n{}".format(relations_dict))
#print("relations_df = \n{}".format(relations_df))
#print("relations_list = \n{}".format(relations_list))

#attributes_dict = loader.attributes('dict')
#attributes_df = loader.attributes('df')
#attributes_list = loader.attributes('list')
#print("attributes_dict = \n{}".format(attributes_dict))
#print("attributes_df = \n{}".format(attributes_df))
#print("attributes_list = \n{}".format(attributes_list))

triples_list = loader.triples('list')
print("triples_list = \n{}".format(triples_list[10]))