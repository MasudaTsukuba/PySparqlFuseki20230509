# import rdflib
from rdflib import Graph, URIRef
from rdflib.plugins import stores
from rdflib.plugins.stores import sparqlstore
from pyfuseki import FusekiQuery
from rdflib.query import ResultParser
from rdflib.plugin import register, Parser


if __name__ == '__main__':
    pass
    register('text/html', Parser, 'rdflib.plugins.parsers.notation3', 'N3Parser')
    fuseki_query = FusekiQuery('http://localhost:3030', 'landmark20230406')
    sparql_str = "SELECT * WHERE { ?s ?p ?o .}"
    query_result = fuseki_query.run_sparql(sparql_str)  # 2024/4/11 Does not work
    print(type(query_result))
    print(query_result)
    pass


    #
    # 追加するRDFトリプルの用意
    bob    = URIRef("http://example.org#bob")
    like   = URIRef("http://example.org#like")
    tomato = URIRef("http://example.org#tomato")
    #
    # # Endpointの用意
    endpoint = r"http://localhost:3030/#/dataset/test20230406/sparql"
    store = stores.sparqlstore.SPARQLUpdateStore()
    store.open((endpoint, r"http://localhost:3030/#/dataset/test20230406/update"))
    pass
    #
    # # 追加するGraph
    default_graph = URIRef('http://example.org/default-graph')
    ng = Graph(store, identifier=default_graph)
    ng.add((bob, like, tomato))  # RDFトリプルに追加
    register('text/html', ResultParser, 'rdflib.query', 'ResultParser')
    results = ng.query('SELECT * WHERE { ?s ?p ?o .}')
    print(results)
    pass
