import requests
import json


response = requests.post('http://localhost:3030/landmark20230406/sparql',
                         data={'query': 'SELECT * WHERE { ?s ?p ?o . } LIMIT 5'})
# response = requests.get('http://localhost:3030/landmark20230406/sparql/?query=SELECT * WHERE{?s ?p ?o.}')
print(response)
for triple in json.loads(response.text)['results']['bindings']:
    print(triple)
pass
