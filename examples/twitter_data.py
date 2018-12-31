from rdfloader import RDFLoader

loader = RDFLoader(sparql_endpoint="", graph_name='http://twitter.com/')
n_e = loader.num_entities()
