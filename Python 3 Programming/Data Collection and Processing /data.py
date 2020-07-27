import requests
import json
params = {'rel_rhy': 'funny'}
r = requests.get('https://api.datamuse.com/words', params)
print('peguei')
print(r.text)
print('-------------')
print(r.url)
print('-------------')
j = r.json()
print(json.dumps(j, indent=2))
