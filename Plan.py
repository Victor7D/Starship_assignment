import requests
import pymongo
from pprint import pprint

def calling_the_api(url: str):
    response = requests.request("GET", url)
    data = response.json()
    return data
pprint(calling_the_api("https://swapi.dev/api/starships/?page=1"))

def find_names_of_pilot(pilot_dic: dict):
    # retuen the name of the pileot


# input: ["https://swapi.dev/api/people/13/","https://swapi.dev/api/people/14/", "https://swapi.dev/api/people/25/","https://swapi.dev/api/people/31/"]
# output: [sam,rob,tom,cam]
def pilot_dict_to_names(list_of_link: list):
    # return the list of names from the links
   """ [
        "https://swapi.dev/api/people/13/",
        "https://swapi.dev/api/people/14/",
        "https://swapi.dev/api/people/25/",
        "https://swapi.dev/api/people/31/"
    ]"""
# input: [sam,rob,tom,cam]
# output: [id1, id2, id3, id4]
def find_id():
    client = pymongo.MongoClient()
    db = client["starwars"]
    # find the name and retuen the id


def add_record_to_colection():
    #add the dict to collection starships

def check_next_page():
    #check if there is a next page or not


def prossing_all_one_page():
    #getting all the record and looping tho so if the key pilots have
    #find the list of pilot names
    #convet the pilot name to ids
    #replace the list with the ids list
    #add the record the colection

def main