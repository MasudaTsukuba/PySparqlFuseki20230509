from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd


working_path = '/home/masuda/PycharmProjects/PySparqlFuseki20230509/'
common_query_path = '/home/masuda/PycharmProjects/PySparqlQuery20230508/query/'


def execute_query(input_file):
    query = ''
    with open(common_query_path+input_file, 'r') as f:
        query = f.read()
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
    sparql.setQuery(query)
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
    sorted_df = df.sort_values(by='s')
    output_file = input_file.replace('.txt', '.csv')
    sorted_df.to_csv(f'{working_path}output_fuseki/{output_file}', index=False)


if __name__ == '__main__':
    # results = execute_query('/home/masuda/PycharmProjects/PySparqlQuery20230508/query/q1.txt')
    # results = execute_query('/home/masuda/PycharmProjects/PySparqlQuery20230508/query/q1pred_build.txt')
    # results = execute_query('/home/masuda/PycharmProjects/PySparqlQuery20230508/query/q6.txt')
    query = 'query_type_object_hotel20230518.txt'
    execute_query(query)
