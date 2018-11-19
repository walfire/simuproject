#### SIMU PROJECT ####

###Libraries###
import numpy as np
import networkx as nx 
import numpy.random as rng
import tkinter as tk
import random

#### CLASSES ####

#### NETWORK STRUCTURE ####

n=1000

#### NETWORK STRUCTURE ####
class Network(object):
    def __init__(self, size=n):
        self.size=size
        self.mean=0
        self.sd=0
        self.dist=0
        self.type=0
        self.agents=[]
        self.inf=[]
        self.gf=nx.Graph()
        self.ginf=nx.DiGraph()
    def generate(self,meanfriends=5, sdfriends=5, frienddist="uni",connectdist="CStyle"):
        for a in range(self.size):
            #
            
            #self.gf.add_node(a,obj=______object_____)
            
            #
            friends=[]
            tar=["r"]
            if frienddist=="uni":
                numf=rng.uniform()
                numf=numf*meanfriends//1+5
                print(numf)
                numf=int(numf)
            if connectdist=="CStyle":
                for a in range(numf):
                    nex=rng.choice(tar)
                    if nex=="r" or nex in friends+["r",a]:
                        while nex in friends+["r",a]:
                            nex=rng.choice(range(self.size))
                    self.gf.add_edge(a,nex)
                    tar=tar+list(self.gf[nex])
                    friends.append(nex)
    def friendsof(self,personnr):
        return(list(self.gf[personnr]))
    def getobj(self,personnr):
        return self.gf.nodes[personnr][obj]
    def draw(self):
        nx.draw(self.gf)
    
#### AGENTS ####

people_total = []
friendship_prob = 0.3
influencer_prob = 0.3
advertising_power = 0.3
comparison_budget = 1000

class Agent:      
    def __init__(self,node_num, friend_list):
        self.node_num = node_num
        self.friends = friend_list
        self.knowngames = {}
        self.preferences = {}
        self.now_playing = 0
        
    def add_friends(self, person):
        self.friends.append(person)
    
    def add_knowngames(self, game, pref=0):
        self.knowngames[game] = pref
    
    def define_preferences(self,likes:dict):
        self.preferences=likes
        
    def get_friends(self):
        return self.friends 
    
    def get_knowngames(self):
        return self.knowngames
    
    def get_preferences(self):
        return self.preferences
    
    def influence_playing(self,key,prob):
        self.knowngames[key] += prob
    
    def recommend(self):
        for i in self.friends:
            i.influence_playing(self.now_playing,friendship_prob)
        
    def game_infection(self):
        for game in sorted(self.knowngames, key=self.knowngames.get, reverse=True):
            prob=self.knowngames[game] 
            if random.choice([0,1],[1-prob,prob]):
                self.now_playing = game
       
class Influencer(Agent):
    def __init__(self):
        self.friends = []
        self.knowngames = {}
        self.preferences = {}
        self.followers = []
        
    def add_followers(self,person):
        self.followers.append(person)
        
    def recommend(self):
        for i in self.followers:
            i.influence_playing(self.now_playing,influencer_prob)
        for i in self.friends:
            i.influence_playing(self.now_playing,friendship_prob)
    
    
#### EFFECTS ON PREFERENCE ####
    
class Advertisement:
    def __init__(self, game, budget):
        self.game = game
        self.budget = budget
        self.effect = advertising_power*self.budget/comparison_budget
        
    def get_effect(self):
        return self.effect   
     
    def run_add(self):
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
    'class that manages the simulation, works with timestamps'
    timeStamp = 0   #accessable from in/outside the class
    
    
    def __init__(self):
        pass

    def networkinit(self):      #Setup
        pass
    def networkfillup(self):
        pass
    def influencernetworkcreation(self):
        pass
    def setupcamesparam(self):
        pass
    def fillupknowngames(self):
        pass
    
    def stateofknowngame(self):     #1 Timestamp
        pass
    def decay(self):
        pass
    def ad(self):
        pass
    def influ(self):
        pass
    def friend(self):
        pass
    def convalgo(self):
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
    
    
