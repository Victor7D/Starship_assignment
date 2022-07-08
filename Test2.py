
"""
                                        The Task:
The data in this database has been pulled from https://swapi.dev/. As well as 'people', the API has data on starships.
In Python, pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship.
Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection.
Use functions at the very least!"""

import pymongo
import requests
from pprint import pprint

"""
This is my get_request function which inputs a url string parameter is my API request.
This outputs it in a json format and makes it more readable"""


def get_request(url: str):
    response = requests.request("GET", url)
    return response.json()


"""
This my is get_id_by_name function which inputs the pilot name as a string.
characters_documents is one object json in mongodb.
Outputs a object_id of the pilot.
                     |
                     v

"""


def get_id_by_name(name: str):
    try:
        client = pymongo.MongoClient()
        db = client["starwars"]
        characters_documents = db.characters.find_one({"name": name})
        # print("cc", characters_documents)
        return characters_documents['_id']
    except TypeError:
        print("Enter a starwars name")


"""
This is my get_pilot_names function which inputs the starship dict from the get request api.
This function looks for the starship pilots list and goes into the list to pull the name 
of the corresponds pilot. With the name it a append it into the new_list_of_names which 
corresponds to pilot url response which it my output.
                     |
                     v
"""


def get_pilot_names(starship: dict) -> list:
    # creates a list of names by looking at the pilots key in the starship json
    new_list_of_names = []
    # starship["pilots"] is a list
    if starship["pilots"]:  # checks if this list is non_empty
        for url in starship["pilots"]:
            res = get_request(url)
            new_list_of_names.append(res["name"])

    return new_list_of_names


"""
This is my replace_links_with_ids function which inputs the starship dict from the get request api.
for each name in the list of names append the ids list with the function get_id_by_name(name) 
which returns the object_id of the pilot. If you uncomment the print("names", names) and 
print("ids", ids) you will see the name and the corresponds object_id.
Now starship["pilots"] replaces what was in the starship, pilots list and make it equal to 
my new ids. Finally it output the new starship json dict which just loops thought to do all starship 
                     |
                     v
"""


def replace_links_with_ids(starship: dict):
    names = get_pilot_names(starship)
    # print("names", names)
    ids = []
    for name_of_pilot in names:
        ids.append(get_id_by_name(name_of_pilot))
    starship["pilots"] = ids
    # print("ids", ids)
    # starship is the new modified json where pilots key contains object ids
    return starship


"""
This is my loading_pipline function. This iterates over each page from the starship api.
it takes each starship object and replaces pilot urls with object ids in mongo db
inserts the new starship objects back into mongodb inside a new collection
                     |
                     v
"""

def loading_pipline():
    url = "https://swapi.dev/api/starships"
    client = pymongo.MongoClient()
    db = client["starwars"]
    while url is not None:
        response = get_request(url)
        starships = response["results"]
        print(starships)
        for starship in starships:
            # print(starship["name"])
            replaced = replace_links_with_ids(starship)
            db.starship.insert_one(replaced)

        print("NEXT PAGE")
        url = response["next"]
        pprint(url)


"""
This is my drop_table function. Which drops the collection in the mongodb.
This for when testing to make sure the documents are not duplicating multiple time.
                     |
                     v
"""

def drop_table():
    client = pymongo.MongoClient()
    db = client["starwars"]
    db.starship.drop()


"Calling the one function makes all the magic happen! "

loading_pipline()