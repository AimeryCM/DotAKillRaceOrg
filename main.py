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
                if player['kills'] is not None:
                    self.kills += player['kills']
                if player['assists'] is not None:
                    self.assists += player['assists']
                if player['deaths'] is not None:
                    self.deaths += player['deaths']
                if player['gold'] is not None and player['gold_spent'] is not None:
                    self.gold += player['gold'] + player['gold_spent']
                if player['denies'] is not None:
                    self.denies += player['denies']
                if player['hero_healing'] is not None:
                    self.healing += player['hero_healing']
                if player['tower_damage'] is not None:
                    self.towerdmg += player['tower_damage']
                if player['hero_damage'] is not None:
                    self.herodmg += player['hero_damage']
                if player['last_hits'] is not None:
                    self.lasthits += player['last_hits']
                if player['obs_placed'] is not None:
                    self.obs += player['obs_placed']
                if player['rune_pickups'] is not None:
                    self.runes += player['rune_pickups']
                if player['sen_placed'] is not None:
                    self.sents += player['sen_placed']
                if player['camps_stacked'] is not None:
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
with open(PLAYER_DATA_FILE) as f1:
    player_data = json.load(f1)

#create a PlayerTotals object for each player in the above json
player_dict = {}

#add PlayerTotals objects to dictionary mapping steamName to PlayerTotals obj
for player in player_data:
    player_dict[player] = PlayerTotals(discord = player_data[player]['Discord'], account_id = player_data[player]['Steam ID'])

#go through the json of submitted matches and add to the PlayerTotals
with open(MATCH_DATA_FILE) as f2:
    match_data = json.load(f2)

for match_info in match_data['Sheet1']:
    currentName = match_info['Steam Name']
    player_dict[currentName].add_match(match_info['MatchID'])


#rank everyone on each part

player_dict["Shifty"].print_stats()
player_dict["Obama Gaming"].print_stats()
player_dict["Xove"].print_stats()
