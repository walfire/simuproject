#### SIMU PROJECT ####

###Libraries###
import numpy as np
import networkx as nx 
import numpy.random as rng
#### CLASSES ####

#written in PSEUDOCODE
#bububububububu
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
    def generate(self,meanfriends=10, sdfriends=5, frienddist="uni",connectdist="CStyle"):
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
    
class Agent:
    friends = []
    #aiiaiaiiaiai
    #jijijijijijij
    #r
    knowngames = {}
    preferences = {}
    #more..
    #ababababababababbabbu


class Person(Agent):    #check on https://www.python-course.eu/python3_inheritance.php 
    pass                   #for inherited classes
    
    
class Influencer(Agent):
    followers = []
    
    
#### EFFECTS ON PREFERENCE ####
    
class Advertisement:
    def effectonperson():
        pass
    def effectoninfluencer():
        pass
    #more?
    
class Influencersinfluence:
    def effectonfollowers():
        pass
    #more?


class Friendsinfluence:
    def effectonfriends():
        pass
    #more?
    

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
#testforbranch
#secondtest
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
    
    
