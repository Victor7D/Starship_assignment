import requests
import pymongo
from pprint import pprint



def calling_the_apis():
    try:
        url = "https://swapi.dev/api/starships/?page=2"
        while url:
            response = requests.request("GET", url)
            data = response.json()
            url = data["next"]
            pprint(response.json()["results"])
    except :
        print("hi")

#pprint(calling_the_apis())

def calling_the_pilots_api():
    url = "https://swapi.dev/api/starships/?page=1"
    response = requests.request("GET", url)
    for pilot in response.json()["results"]:
        for i in pilot["pilots"]:
            print(i)

pprint(calling_the_pilots_api())
