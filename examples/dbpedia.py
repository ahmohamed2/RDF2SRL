from rdf2srl import RDFGraphDataset

if __name__ == "__main__":
    loader = RDFGraphDataset(sparql_endpoint="http://dbpedia.org/sparql")
    m = loader.num_triples()
    print("m = {}".format(m))
    #n_e = loader.num_entities()
    #print("n_e = {}".format(n_e))


