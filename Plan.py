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

    # print(get_id_by_name("Boba Fett"))

    def get_pilot_names(starship):
        new_list_of_names = []
        if starship["pilots"]:
            for url in starship["pilots"]:
                res = get_request(url)
                new_list_of_names.append(res["name"])

        return new_list_of_names

    # print(get_pilot_names())

    def replace_links_with_ids(starship):
        names = get_pilot_names(starship)
        ids = []
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
                db.starship.insert_one(replaced)  # put_starship_in_db(replaced)

            print("NEXT PAGE")
            url = response["next"]
            pprint(url)

    def drop_table():
        client = pymongo.MongoClient()
        db = client["starwars"]
        db.starship.drop()

    loading_elt_pipline()
