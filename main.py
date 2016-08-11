from collections import defaultdict
from threading import Thread

import pgoapi
import configparser
import time

import glob

import sys


def parse_configfile(path):
    config = configparser.ConfigParser()
    config.read(path)

    service = config["Authentication"]["Service"]
    username = config["Authentication"]["Username"]
    password = config["Authentication"]["Password"]

    Api = pgoapi.PGoApi()
    ans = Api.login(service, username, password, 44.623, 7.623, 0)
    if ans:
        print("Logged in as "+username)
    else:
        print("Login as %s failed. Exiting..." % username)
        sys.exit(1)
    time.sleep(2)

    return Api


def rename_mons(Api):
    inventory = Api.get_inventory()['responses']
    inventory = inventory["GET_INVENTORY"]["inventory_delta"]["inventory_items"]

    inventory = [i['inventory_item_data'] for i in inventory]

    # inventory contains items, candies, pokemon, pokedex entries... -> remove everything but pokemon
    inventory = list(filter(lambda x: 'pokemon_data' in x, inventory))

    pokemons = [i['pokemon_data'] for i in inventory]  # get data
    # pokemons = [p for p in pokemons if 'nickname' not in p]  # don't change nickname
    pokemons = list(filter(lambda x: 'is_egg' not in x, pokemons))  # remove eggs
    pokemons = [defaultdict(int, p) for p in pokemons]  # replace missing keys with 0

    for pokemon in pokemons:
        a = pokemon['individual_attack']
        d = pokemon['individual_defense']
        s = pokemon['individual_stamina']

        percentage = int( ((a+d+s)/45)*100 )

        print("Renaming pokemon: [%s]. " % str(pokemon['pokemon_id']), end="")
        if percentage < 85:
            print("It sucks!")
        else:
            print("Percentage is: "+str(percentage))

        nickname = "{percentage}% {a}/{d}/{s}".format(**locals())
        # nickname = str(pokemon['individual_attack']+pokemon['individual_defense']+pokemon['individual_stamina'])
        Api.nickname_pokemon(pokemon_id=pokemon['id'], nickname=nickname)
        time.sleep(1)
    print("Done - Renamed %s mons!" % len(pokemons))

def bot(path):
    Api = parse_configfile(path)
    rename_mons(Api)


for path in glob.glob("config/*.ini"):
    Thread(target=bot, args=(path,)).start()
    time.sleep(5)