import requests
from pprint import pprint

url = 'http://api.open-notify.org/astros.json'

limit_of_astronauts = requests.get(url)
limit = limit_of_astronauts.json()

params = {
    'limit': limit['number'],
    'skip': 0,
}

response = requests.get(url=url, params=params)
result = response.json()

astronauts = result['people']
list_of_astronauts = []

for astronaut in astronauts:
    name = astronaut['name']
    list_of_astronauts.append(name)

pprint(list_of_astronauts)
