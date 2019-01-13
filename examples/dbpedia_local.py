import sys
sys.path.append('/home/amohamed/RDF2SRL/')
from rdf2srl.rdfloader import RDFGraphDataset

loader = RDFGraphDataset(sparql_endpoint="http://192.168.10.2:8890/sparql", graph_name='http://dbpedia.org/')

predicates_freq_df = loader.predicates_freq()
print(predicates_freq_df)