#### SIMU PROJECT ####


#### CLASSES ####



#### NETWORK STRUCTURE ####
import random

people_total = []

class Agent:    
    
    friendship_prob = 0.3
    
    def __init__(self,node_num, friend_list):
        self.node_num = node_num
        self.friends = friend_list
        self.knowngames = {}
        self.preferences = {}
        self.now_playing = 0
        
    def self.add_friends(self, person):
        self.friends.append(person)
    
    def self.add_knowngames(self, game, pref=0):
        self.knowngames[game] = pref
    
    def self.define_preferences(self,likes:dict):
        self.preferences=likes
        
    def self.get_friends(self):
        return self.friends 
    
    def self.get_knowngames(self):
        return self.knowngames
    
    def self.get_preferences(self):
        return self.preferences
    
    def self.influence_playing(self,key,prob):
        self.knowngames[key] += prob
    
    def self.recommend():
        for i in self.friends:
            i.influence_playing(self.now_playing,friendship_prob)
        
    def self.game_infection(self):
        for game in sorted(self.knowngames, key=self.knowngames.get, reverse=True):
            prob=knowngames[game] 
            if random.choice([0,1],[1-prob,prob]):
                self.now_playing = game
       
class Influencer(Agent):
    influencer_prob = 0.3
    def __init__(self):
        self.friends = []
        self.knowngames = {}
        self.preferences = {}
        self.followers = []
        
    def self.add_followers(self,person):
        self.followers.append(person)
        
    def self.recommend():
        for i in self.followers:
            i.influence_playing(self.now_playing,influencer_prob)
        for i in self.friends:
            i.influence_playing(self.now_playing,friendship_prob)
    
    
#### EFFECTS ON PREFERENCE ####
    
class Advertisement:
    comparison_budget = 1000
    advertising_power = 0.3
    def __init__(self, game, budget):
        self.game = game
        self.budget = budget
        self.effect = advertising_power*self.budget/comparison.budget
        
    def self.get_effect(self):
        return self.effect   
     
    def self.run_add():
        for i in people_total:
            i.influence_playing(self.game, self.effect)
        

#### GAME ####
    
    
class Game:
    decay = 0
    popularity = 0.0
    budget = 0.0
    multiplayer = 0.0
    singleplayer = 0.0
    mainstream = 0.0
    target = 0.0 #niche - mainstream
    team = ["indie","blockbuster"] #optional?
    #more?
    
    
    
#### CONVERSION ALGORITHM ####
    
class Conversionalgo:
    def findpercent():
        pass
    def activeagent():
        pass
    def passiveagent():
        pass
    def decidegameplayed():
        pass
    #more?

#### SIMULATION MANAGER ####

class Simumanager:
    def networkinit():      #Setup
        pass
    def networkfillup():
        pass
    def influencernetworkcreation():
        pass
    def setupcamesparam():
        pass
    def fillupknowngames():
        pass
    
    def stateofknowngame():     #1 Timestamp
        pass
    def decay():
        pass
    def ad():
        pass
    def influ():
        pass
    def friend():
        pass
    def convalgo():
        pass
    
#### DATA MANAGER ####

class Datamanager:
    def savenetwork():
        pass
    def savecurrenttimestamp():
        pass
    
    
#### PLOTTER ####
        
class plotter:
    def setupplot():
        pass
    def drawnodes():
        pass
    def drawedges(node, depth):     #node: person & influencer, depth: how many levels of friends of friends of frieds i.e.
        pass
    def update():
        pass
    def exportplot():
        pass
    #more?
    
    
