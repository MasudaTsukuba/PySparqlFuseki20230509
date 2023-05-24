from rdflib import Graph
import pandas as pd
import os

working_path = os.getcwd()
if working_path.endswith('src'):
    working_path = os.path.dirname(working_path)
# common_query_path = os.path.dirname(working_path)+'/PySparqlQuery20230508/'
common_query_path = os.path.dirname(working_path)+'/PySparqlSatoNew20230509/query/'


def read_rdf():
    g = Graph()
    g.parse(f'{working_path}/graph/graph_all.ttl')
    length = len(g)
    pass
    return g


def read_query(query):
    file_name = f'{common_query_path}query/{query}'
    # input_query = ''
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
    my_vars = []
    for var in sparql_results.vars:
        my_vars.append(str(var))
    df = pd.DataFrame(results, columns=my_vars)
    pass
    return df


def execute_query(query):
    g = read_rdf()
    input_query = read_query(query)
    sparql_results = g.query(input_query)
    print(len(sparql_results.bindings))
    df = convert_results(sparql_results)
    sorted_df = df.sort_values(by='s')
    output_file = query.replace('.txt', '.csv')
    sorted_df.to_csv(f'{working_path}/output_rdf/{output_file}', index=False)
    pass
    return sparql_results.bindings


if __name__ == "__main__":
    # execute_query('q1.txt')
    # execute_query('q1pred.txt')
    # execute_query('q1pred_build.txt')
    # execute_query('q2.txt')
    # execute_query('q3a.txt')
    # execute_query('q3b.txt')
    # execute_query('q4.txt')
    # execute_query('q5.txt')
    # execute_query('q6.txt')
    # execute_query('q7.txt')
    query = 'query_type_object_hotel20230518.txt'
    execute_query(query)
