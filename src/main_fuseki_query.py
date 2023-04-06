# import rdflib
from rdflib import Graph, URIRef
from rdflib.plugins import stores
from rdflib.plugins.stores import sparqlstore
import requests
from SPARQLWrapper import SPARQLWrapper, JSON, SPARQLWrapper2

if __name__ == '__main__':
    # sparql = SPARQLWrapper2("http://localhost:3030/#/dataset/test20230404/query")
    #
    # sparql.setQuery("""
    # SELECT * WHERE {
    # ?s ?p ?o.
    # }
    # """)
    # sparql.setReturnFormat(JSON)
    # try:
    #     for result in sparql.query().bindings:
    #         print(result)
    #     # ret = sparql.queryAndConvert()
    #     #
    #     # for r in ret["results"]["bindings"]:
    #     #     print(r)
    # except Exception as e:
    #     print(e)
    # response = requests.post('http://localhost:3030/#/dataset/test20230404/query',
    #                          data={'query': 'ASK { ?s ?p ?o . }'})
    # print(response)
    #
    # 追加するRDFトリプルの用意
    bob    = URIRef("http://example.org#bob")
    like   = URIRef("http://example.org#like")
    tomato = URIRef("http://example.org#tomato")

    # Endpointの用意
    endpoint = r"http://localhost:3030/#/dataset/test20230404/query"
    store = stores.sparqlstore.SPARQLUpdateStore()
    store.open((endpoint, r"http://localhost:3030/#/dataset/test20230404/update"))

    # 追加するGraph
    default_graph = URIRef('http://example.org/default-graph')
    ng = Graph(store, identifier=default_graph)
    # ng.add((bob, like, tomato))  # RDFトリプルに追加
    results = ng.query('SELECT * WHERE { ?s ?p ?o .}')
    # print(results.bindings)
