from SPARQLWrapper import SPARQLWrapper, JSON, SPARQLWrapper2


sparql = SPARQLWrapper2("http://localhost:3030/landmark20230406/sparql")

sparql.setQuery("""
SELECT * WHERE {
?s ?p ?o.
} LIMIT 10
""")
sparql.setReturnFormat(JSON)
try:
    for result in sparql.query().bindings:
        print(result)
    # ret = sparql.queryAndConvert()
    #
    # for r in ret["results"]["bindings"]:
    #     print(r)
except Exception as e:
    print(e)
pass
