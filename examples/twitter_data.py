import sys
sys.path.append('/home/amohamed/RDF2SRL/')
from rdfloader import RDFGraphDataset

loader = RDFGraphLoader(sparql_endpoint="http://192.168.10.2:8890/sparql", graph_name='http://twitter.com/')

n_e = loader.num_entities()
n_p = loader.num_predicates()
n_r = loader.num_relations()
n_a = loader.num_attributes()
n_al = loader.num_attr_literal_pairs()
m = loader.num_triples() # 49223643
print("n_e = {}  n_p = {}  n_r = {}  n_a = {}  n_al = {}  m = {}".format(n_e, n_p, n_r, n_a, n_al, m))
e2l_m = loader.num_entity2literal_triples()
e2e_m = loader.num_entity2entity_triples()
print("num_entity2entity_triples = {}  num_entity2literal_triples = {}".format(e2e_m, e2l_m))
print("m = {}  e2l_m+e2e_m = {}".format(m, e2l_m+e2e_m))

assert(e2l_m+e2e_m == m)

#predicates_dict = loader.predicates('dict')


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