#### SIMU PROJECT ####

###Libraries###
import numpy as np
import networkx as nx 
import numpy.random as rng
import tkinter as tk
import random

#### CLASSES ####

#### NETWORK STRUCTURE ####

n=100

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
        self.infperag=1
        self.numinf=10
    def generate(self,meanfriends=5, sdfriends=5, frienddist="uni",connectdist="CStyle"):
        for a in range(self.size):
            self.gf.add_node(a,obj="______object_____")
        if connectdist=="CStyle":
            for a in range(self.size):
                #
                
                #self.gf.add_node(a,obj=______object_____)
                
                #
                tar=["r"]
                friends=[]
                for b in list(self.gf[a]):
                    friends.append(b)
                    for c in list(self.gf[b]):
                        tar.append(c)
                    
                
                if frienddist=="uni":
                    #numf=rng.uniform()
                    #numf=numf*meanfriends//1+5
                    numf=10
                    #numf=15-len(friends)
                    #if numf <0:
                     #   numf=1
                    numf=int(numf)
                if connectdist=="CStyle":
                    for aa in range(numf):
                        nex=rng.choice(tar)
                        if nex=="r" or int(nex) in friends+["r",a]:
                            while nex in friends+["r",a] or int(nex) in friends+["r",a]:
                                nex=int(rng.choice(range(self.size)))
                        nex=int(nex)
                        self.gf.add_edge(a,int(nex))
                        tar=tar+list(self.gf[nex])
                        friends.append(nex)
                if len(self.gf[a])<5:
                    print(a)
                    print(friends)
                    print(self.gf[a])
                    print(" \n")
        if connectdist=="randomunif":
            #notperfect
            numf=10
            connect={k:[] for k in range(self.size)}
            li=[]
            for a in range(self.size-1):
                it=0
                while len(connect[a])<numf and it<100:
                    it+=1
                    r=rng.choice(range(a+1,self.size))
                    if len(connect[r])<10 or r in connect[a]:
                        #print(a,r)
                        li.append([int(a),int(r)])
                        connect[a].append(r)
                        connect[r].append(a)
                print(a,it,len(connect[a]))
            print(len(li))
            for b,c in li:    
                self.gf.add_edge(b,c)
                #gnm_random_graph(n, m, seed=None, directed=False)
                #connected_watts_strogatz_graph(n, k, p[, ...])
            #if len(self.gf[a])<5:
             #   print(a)
              #  print(friends)
               # print(self.gf[a])
                #print(" \n")
        if connectdist=="randomunif2":
            al=[]
            numf=10
            for a in range(numf):
                al=al+list(range(self.size))
            con=[]
            al2=al
            rng.shuffle(al2)
            it=0
            while it<10000:
                it+=1
                if len(al2)>=1:
                    cand=al2[:2]
                    if cand[0]!=cand[1] and cand not in con and cand[::-1] not in con:
                        con.append(frozenset(al2[:2]))
                        al2=al2[2:]
                    else:
                        rng.shuffle(al2)
                else:
                    break
            print(con,len(con),len(set(con)),it)
            for b,c in con:    
                self.gf.add_edge(b,c)
        if connectdist=="prederd":
            n=self.size
            k=10/(n-1)
            te=nx.gnp_random_graph(n,k)
            print(te.edges)
                #dic={}
                #for a in range(self.size):
                #    dic[a]=self.gf.nodes[a][obj]
                #nx.set_node_attributes(te,dic,"obj")                    
                #self.gf=te  
            self.gf.add_edges_from(te.edges)
                
                
                #karate_club_graph()
    def friendsof(self,personnr):
        return(list(self.gf[personnr]))
    def getobj(self,personnr):
        return self.gf.nodes[personnr][obj]
    def draw(self):
        nx.draw(self.gf)
    def addinf(self):
        #choose numinf randomagents as infs
        #loop over agents 
        # generate score for each inf according to taste similarity
        # chose infperag ones according to score
        pass
        #probably output a dic of ags per inf, but also add inf as a trait of ag
        
        

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
    
    
