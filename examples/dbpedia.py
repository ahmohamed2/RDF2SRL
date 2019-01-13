from rdf2srl.rdfloader import RDFGraphDataset

if __name__ == "__main__":
    loader = RDFGraphDataset(sparql_endpoint="http://dbpedia.org/sparql/")
    m = loader.num_triples()

    n_e = loader.num_entities() # 5,250,147
    n_p = loader.num_predicates() # 30
    n_r = loader.num_relations() # 10
    n_a = loader.num_attributes() # 20
    n_al = loader.num_attr_literal_pairs() # 14,449,483

    print("n_e = {}  n_p = {}  n_r = {}  n_a = {}  n_al = {}  m = {}".format(n_e, n_p, n_r, n_a, n_al, m))

    e2l_m = loader.num_entity2literal_triples() # 32,427,451 OR 32,676,993
    e2e_m = loader.num_entity2entity_triples()
    num_rdf_type_triples = loader.num_rdf_type_triples()
    print("num_entity2entity_triples = {}".format(e2e_m)) 
    print("num_entity2literal_triples = {}".format(e2l_m)) # 17,656,907
    print("num_rdf_type_triples = {}".format(num_rdf_type_triples)) # 5,250,147
    print("m = {}  e2l_m+e2e_m = {}".format(m, e2l_m+e2e_m))

    predicates_df = loader.predicates('df')
    print("predicates_df = \n{}".format(predicates_df))

    relations_df = loader.relations('df')
    print("relations_df = \n{}".format(relations_df))

    attributes_df = loader.attributes('df')
    print("attributes_df = \n{}".format(attributes_df))

    entities_df = loader.entities('df') # len = 5,250,147 

    triples_list = loader.triples('list')
    print("triples_list sample = \n{}".format(triples_list[:10]))

