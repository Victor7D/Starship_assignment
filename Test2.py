import pymongo
import requests
from pprint import pprint

"""
This function is my API request.
That converts it to json format and makes it more readable"""

def get_request(url):
    response = requests.request("GET", url)
    return response.json()


"""
So what this function is doing is it's using the mongo DB Starship database 
and finding ID of Star Wars character name. """

def get_id_by_name(name):
    client = pymongo.MongoClient()
    db = client["starwars"]
    dv = db.characters.find_one({"name": name})
    return dv['_id']
#print(get_id_by_name("Boba Fett"))



def get_pilot_names(starship):
    new_list_of_names = []
    if starship["pilots"]:
        for url in starship["pilots"]:
            res = get_request(url)
            new_list_of_names.append(res["name"])

    return new_list_of_names
#print(get_pilot_names())



def replace_links_with_ids(starship):
    names = get_pilot_names(starship)
    ids =[]
    for name in names:
        ids.append(get_id_by_name(name))
    starship["pilots"] = ids
    return starship


def loading_elt_pipline():
    url = "https://swapi.dev/api/starships"
    client = pymongo.MongoClient()
    db = client["starwars"]
    while url is not None:
        response = get_request(url)
        starships = response["results"]
        print(starships)
        for starship in starships:
            replaced = replace_links_with_ids(starship)
            db.starship.insert_one(replaced) #put_starship_in_db(replaced)

        print("NEXT PAGE")
        url = response["next"]
        pprint(url)

def drop_table():
    client = pymongo.MongoClient()
    db = client["starwars"]
    db.starship.drop()


loading_elt_pipline()

#if __name__ == "__main__":
