import requests
import json


response = requests.post(
    'http://localhost:3030/landmark20230518/sparql',
    # data={'query': 'SELECT * WHERE { ?s ?p ?o . } LIMIT 5'})
    data={'query':
          'SELECT ?s ?type WHERE { ?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type . }'})
# response = requests.get('http://localhost:3030/landmark20230406/sparql/?query=SELECT * WHERE{?s ?p ?o.}')
results = json.loads(response.text)['results']['bindings']
print(len(results))
for triple in results:
    # print(triple)
    pass
