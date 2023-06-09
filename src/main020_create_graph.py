from rdflib import Graph
import os


def read_rdf():
    g = Graph()
    # g = Graph(store='BerkeleyDB')
    rdf_files = os.listdir('../rml_rdf/')  # all files in rml_rdf folder
    for file in rdf_files:
        if file.endswith('.ttl'):  # if the file name ends with .ttl
            print(file)
            g.parse(f'../rml_rdf/{file}')  # read into a graph
    length = len(g)
    pass
    return g


if __name__ == "__main__":
    g = read_rdf()
    g.serialize('../graph/graph_all.ttl')
