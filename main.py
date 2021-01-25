import requests
import json

OPENDOTA_URL = "https://api.opendota.com/api/matches/"
MATCH_DATA_FILE = "./match_data.json"
PLAYER_DATA_FILE = "./player_data.json"

class PlayerTotals():

    # The object to hold the totals for all of the player stats

    def __init__(self, discord, account_id, kills = 0, assists = 0, deaths = 0, gold = 0, denies = 0, healing = 0, towerdmg = 0, herodmg = 0, lasthits = 0, obs = 0, runes = 0, sents = 0, stacks = 0):
        self.discord = discord
        self.account_id = account_id
        self.kills = kills
        self.assists = assists
        self.deaths = deaths
        self.gold = gold
        self.denies = denies
        self.healing = healing
        self.towerdmg = towerdmg
        self.herodmg = herodmg
        self.lasthits = lasthits
        self.obs = obs
        self.runes = runes
        self.sents = sents
        self.stacks = stacks
    
    def add_match(self, matchID):
        response = requests.get(OPENDOTA_URL + str(matchID))
        response_json = response.json()
        players_obj = response_json['players']
        for player in players_obj:
            this_account_id = player["account_id"]
            if self.account_id == this_account_id:
                self.kills += player['kills']
                self.assists += player['assists']
                self.deaths += player['deaths']
                self.gold += player['gold'] + player['gold_spent']
                self.denies += player['denies']
                self.healing += player['hero_healing']
                self.towerdmg += player['tower_damage']
                self.herodmg += player['hero_damage']
                self.lasthits += player['last_hits']
                self.obs += player['obs_placed']
                self.runes += player['rune_pickups']
                self.sents += player['sen_placed']
                self.stacks += player['camps_stacked']

    def print_stats(self):
        print("discord: " + self.discord)
        print("steamID: " + str(self.account_id))
        print("kills: " + str(self.kills))
        print("assists: " + str(self.assists))
        print("deaths: " + str(self.deaths))
        print("gold: " + str(self.gold))
        print("denies: " + str(self.denies))
        print("healing: " + str(self.healing))
        print("towerdmg: " + str(self.towerdmg))
        print("herodmg: " + str(self.herodmg))
        print("lasthits: " + str(self.lasthits))
        print("obs: " + str(self.obs))
        print("runes: " + str(self.runes))
        print("sents: " + str(self.sents))
        print("stacks: " + str(self.stacks))



#main

#import json of player info. will convert steam name to ID and discord name

#create a PlayerTotals object for each player in the above json

#add PlayerTotals objects to dictionary mapping steamID to PlayerTotals obj

#go through the json of submitted matches and add to the PlayerTotals

#rank everyone on each part

test_obj = PlayerTotals("Shifty#9661", 84853139)
test_obj.add_match(5799792595)
test_obj.print_stats()
