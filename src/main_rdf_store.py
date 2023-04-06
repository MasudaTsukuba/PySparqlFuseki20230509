# from rdflib import ConjunctiveGraph, Namespace, Literal
# from rdflib.store import NO_STORE, VALID_STORE
from rdflib import Graph

# use the default memory Store
graph = Graph()

# use the BerkeleyDB Store
graph = Graph(store="BerkeleyDB")
# graph = ConjunctiveGraph('Sleepycat')

# rt = graph.open("C:\Users\Maral\Desktop\Springer-DBLP\Mydblp", create=False)
#
# if rt == NO_STORE:
#     # There is no underlying Sleepycat infrastructure, create it
#     graph.open(path, create=True)
# else:
#     assert rt == VALID_STORE, 'The underlying store is corrupt'
#
# print('Triples in graph before add: ', len(graph))
#
# ontologies = rdflib.Graph()
# ontologies.parse('C:\Users\Maral\Desktop\dblp.rdf',format='xml')
# for onto in ontologies:
#     graph.add(onto)
# print ('Triples in graph after add: ', len(graph))
#
# print (graph.serialize(format='xml'))
#
# # close when done, otherwise sleepycat will leak lock entries.
# graph.close()
