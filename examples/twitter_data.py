import sys
sys.path.append('/home/amohamed/RDF2SRL/')
from rdfloader import RDFGraphDataset

loader = RDFGraphDataset(sparql_endpoint="http://192.168.10.2:8890/sparql", graph_name='http://twitter.com/')

n_e = loader.num_entities()
print("n_e = {}".format(n_e))
n_p = loader.num_predicates()
print("n_p = {}".format(n_p))
n_r = loader.num_relations()
print("n_r = {}".format(n_r))
n_a = loader.num_attributes()
print("n_a = {}".format(n_a))
n_al = loader.num_attr_literal_pairs()
print("n_al = {}".format(n_al))
m = loader.num_triples() # 49223643
print("m = {}".format(m))

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