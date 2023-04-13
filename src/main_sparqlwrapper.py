from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    "http://localhost:3030/landmark20230406/sparql"
)
sparql.setReturnFormat(JSON)

# gets the first 3 geological ages
# from a Geological Timescale database,
# via a SPARQL endpoint
sparql.setQuery("""
    SELECT *
    WHERE {
        ?s ?p ?o .
    }
    LIMIT 10
    """
)

try:
    ret = sparql.queryAndConvert()
    # print(ret)
    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)
