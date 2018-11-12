#### SIMU PROJECT ####


#### CLASSES ####

#written in PSEUDOCODE
#bububububububu

#### NETWORK STRUCTURE ####

class Agent:
    friends = []
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
    
    
