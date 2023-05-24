from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import os

working_path = os.getcwd()
if working_path.endswith('src'):
    working_path = os.path.dirname(working_path)
# common_query_path = os.path.dirname(working_path)+'/PySparqlQuery20230508/'
common_query_path = os.path.dirname(working_path)+'/PySparqlSatoNew20230509/query/'


def execute_query(input_file):
    sparql_query = ''
    with open(common_query_path+input_file, 'r') as f:
        sparql_query = f.read()
    sparql = SPARQLWrapper(
        "http://localhost:3030/landmark20230518/sparql"
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
    sparql.setQuery(sparql_query)
    print(sparql_query)
    ret = None
    try:
        ret = sparql.queryAndConvert()
        # print(ret)
        # for r in ret["results"]["bindings"]:
        #     print(r)
    except Exception as e:
        print(e)
    sparql_results = ret['results']['bindings']
    print(len(sparql_results))
    # my_vars = []
    # for var in ret['head']['vars']:
    #     my_vars.append(str(var))

    def convert_results(sparql_results_arg):
        results = []
        for binding in sparql_results_arg['results']['bindings']:
            result = []
            for item in binding.items():
                result.append(str(item[1]['value']))
            results.append(result)
        my_vars_tmp = []
        for var_tmp in sparql_results_arg['head']['vars']:
            my_vars_tmp.append(str(var_tmp))
        df_tmp = pd.DataFrame(results, columns=my_vars_tmp)
        return df_tmp

    df = convert_results(ret)
    header = df.columns
    keys = []
    for element in header:
        keys.append(element)
    sorted_df = df.sort_values(by=keys)
    output_file = input_file.replace('.txt', '.csv')
    sorted_df.to_csv(f'{working_path}/output_fuseki/{output_file}', index=False)

    return sparql_results


if __name__ == '__main__':
    # results = execute_query('/home/masuda/PycharmProjects/PySparqlQuery20230508/query/q1.txt')
    # results = execute_query('/home/masuda/PycharmProjects/PySparqlQuery20230508/query/q1pred_build.txt')
    # results = execute_query('/home/masuda/PycharmProjects/PySparqlQuery20230508/query/q6.txt')
    # query = 'q1.txt'
    # query = 'q5.txt'
    query = 'q5b.txt'
    # query = 'q1pred_hotel.txt'
    # query = 'q1pred_build.txt'
    # query = 'query_extract_museums20230519.txt'
    # query = 'query_extract_buildings20230519.txt'
    # query = 'query_extract_heritages20230519.txt'
    # query = 'query_extract_hotels_with_name20230519.txt'
    # query = 'query_extract_labels20230519.txt'
    # query = 'query_type_object_hotel20230518.txt'
    query = 'q1pred_get_hotel.txt'
    execute_query(query)
