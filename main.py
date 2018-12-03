#### SIMU PROJECT ####

###Libraries###
import numpy as np
import networkx as nx 
import Tkinter as tk


#### CLASSES ####

#written in PSEUDOCODE
#bububububububu

#### NETWORK STRUCTURE ####

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

#https://www.tutorialspoint.com/python/python_classes_objects.htm
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/

class Simumanager:
    'class that manages the simulation & works with timestamps'
    timeStamp = 0   #accessable from in/outside the class
    
    def quitsimu(self):
        self.window.destroy()
        
    
    window = tk.Tk()                    #GUI of the simumanager
    window.title("Simulation Manager")
    window.geometry('800x600')
    
    quitbutton = tk.Button(window, text="Quit", command = quitsimu())
    quitbutton.grid(column=100, row=100)
    
    window.mainloop()
    
    def __init__(self):
        Simumanager.timeStamp = 0 #init the timestamp to 0 for a new simulation
        
        
    


    def loadsimu(self, timestamp, datafile):
        Simumanager.timeStamp = timestamp
        
    def networkinit(self):      #Setup
        pass
    def networkfillup(self):
        pass
    def influencernetworkcreation(self):
        pass
    def setupgamesparam(self):
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
    
    
Simumanager()
