import sys
sys.path.append('/home/amohamed/RDF2SRL/')
from rdf2srl.smartloader import SmartRDFGraphDataset

loader = SmartRDFGraphDataset(sparql_endpoint="http://192.168.10.2:8890/sparql",
	graph_name='http://dbpedia.org/')
n_e = loader.num_entities()  #
print("n_e = {}".format(n_e))
m = loader.num_triples()  #
print("num_triples = {}".format(m))
ne_e2e = loader.num_entity2entity_triples()
print("num_entity_to_entitiy_triples = {}".format(ne_e2e))
n_p = loader.num_predicates()  #
print("num_predicates = {}".format(n_p))
n_r = loader.num_relations()  #
print("num_relations = {}".format(n_r))
n_a = loader.num_attributes()  #
print("num_attributes = {}".format(n_a))
n_al = loader.num_attr_literal_pairs()  #
print("num_Attribute_literal)pairs = {}".format(n_al))

triples_df = loader.entity2entity_triples(return_format='df', output_dir=None)
print(triples_df.head(10))
print("size of entity to entity triples = {}".format(triples_df.shape))

predicates_freq_df = loader.predicates_freq()
print(predicates_freq_df)