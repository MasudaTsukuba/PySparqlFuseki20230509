from rdflib import Graph
import pandas as pd


def read_rdf():
    g = Graph()
    g.parse(f'/home/masuda/PycharmProjects/PySparqlFuseki20230501/graph/graph_all.ttl')
    length = len(g)
    pass
    return g


def read_query(query):
    file_name = f'/home/masuda/PycharmProjects/PySparqlQuery20230508/query/{query}'
    input_query = ''
    with open(file_name, 'r') as f:
        input_query = f.read()
    # input_query = """
    # PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    # PREFIX ex: <http://example.com/ontology/>
    # PREFIX country: <http://example.com/predicate/country>
    # PREFIX country_name: <http://example.com/predicate/country_name>
    # PREFIX country_comment: <http://example.com/predicate/country_comment>
    #
    # SELECT ?s ?name
    # WHERE {
    #     ?s rdf:type ex:Hotel.
    #     ?s rdf:label ?name.
    # }
    # """
    return input_query


def convert_results(sparql_results):
    results = []
    for binding in sparql_results.bindings:
        result = []
        for item in binding.items():
            result.append(str(item[1]))
        results.append(result)
    vars = []
    for var in sparql_results.vars:
        vars.append(str(var))
    df = pd.DataFrame(results, columns=vars)
    pass
    return df


def execute_query(query):
    g = read_rdf()
    input_query = read_query(query)
    sparql_results = g.query(input_query)
    print(len(sparql_results.bindings))
    df = convert_results(sparql_results)
    output_file = query.replace('.txt', '.csv')
    df.to_csv(f'/home/masuda/PycharmProjects/PySparqlFuseki20230501/output/{output_file}', index=False)
    pass
    return sparql_results.bindings


if __name__ == "__main__":
    # execute_query('q1.txt')
    # execute_query('q1pred.txt')
    execute_query('q1pred_build.txt')
    # execute_query('q2.txt')
    # execute_query('q3a.txt')
    # execute_query('q3b.txt')
    # execute_query('q4.txt')
    # execute_query('q5.txt')
    # execute_query('q6.txt')
    # execute_query('q7.txt')
