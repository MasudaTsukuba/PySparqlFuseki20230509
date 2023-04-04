from rdflib import Graph
import os


def read_rdf():
    g = Graph()
    rdf_files = os.listdir('../rml_rdf/')
    for file in rdf_files:
        if file.endswith('.ttl'):
            print(file)
            g.parse(f'../rml_rdf/{file}')
    length = len(g)
    pass
    return g


if __name__ == "__main__":
    g = read_rdf()
    g.serialize('../graph/graph_all.ttl')
