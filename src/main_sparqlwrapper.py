from SPARQLWrapper import SPARQLWrapper, JSON


def execute_query(input_file):
    query = ''
    with open(input_file, 'r') as f:
        query = f.read()
    sparql = SPARQLWrapper(
        "http://localhost:3030/landmark20230406/sparql"
    )
    sparql.setReturnFormat(JSON)

    # gets the first 3 geological ages
    # from a Geological Timescale database,
    # via a SPARQL endpoint
    # sparql.setQuery("""
    #     SELECT *
    #     WHERE {
    #         ?s ?p ?o .
    #     }
    #     LIMIT 10
    #     """
    # )
    sparql.setQuery(query)
    ret = None
    try:
        ret = sparql.queryAndConvert()
        # print(ret)
        # for r in ret["results"]["bindings"]:
        #     print(r)
    except Exception as e:
        print(e)
    return ret['results']['bindings']


if __name__ == '__main__':
    results = execute_query('../query/q1.txt')
    print(len(results))
