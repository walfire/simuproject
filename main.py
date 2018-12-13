#### SIMU PROJECT ####

###Libraries###
import numpy as np
import networkx as nx 
import numpy.random as rng

import random


#### CLASSES ####

#### NETWORK STRUCTURE ####

n=100
keys=["complex" , "friendly" , "meaning", "polish" , "multi", "action", "difficulty", "abstract"]
def getscore(dic1,dic2):
            #used in influencer assignment
    sco=0
    for a in keys:
        sco+=abs(dic1[a]-dic2[a])
    sco=(1-sco/len(keys))*100
    return sco
#### NETWORK STRUCTURE ####
class Network(object):
    def __init__(self, size=n):
        self.size=size
        self.mean=0
        self.sd=0
        self.watchers=[]
        self.dist=0
        self.type=0
        self.agentsid=[]
        self.agents=[]
        self.inf=[]
        self.gf=nx.Graph()
        #not sure if dgraph is still needed. if just doesnt work, try graph witout di
        self.ginf=nx.DiGraph()
        self.infperag=1
        self.numinf=10
        self.infdic={}
        self.infobj=[]
        
    def generate(self,meanfriends=5, sdfriends=5, frienddist="uni",connectdist="CStyle"):
                #generates object and the f network
        for a in range(self.size):
            self.gf.add_node(a,obj=Agent(a))
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
                    numf=5
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
        if connectdist=="watstro":
            n=self.size
            p=0.2
            k=10
            te=nx.connected_watts_strogatz_graph(n,k,p,100)
                #dic={}
                #for a in range(self.size):
                #    dic[a]=self.gf.nodes[a][obj]
                #nx.set_node_attributes(te,dic,"obj")                    
                #self.gf=te  
            self.gf.add_edges_from(te.edges)
        if connectdist=="full":
            n=self.size
            e=[]
            for a in range(n-1):
                for b in range(a+1,n):
                    e.append(set([a,b]))
                #dic={}
                #for a in range(self.size):
                #    dic[a]=self.gf.nodes[a][obj]
                #nx.set_node_attributes(te,dic,"obj")                    
                #self.gf=te  
            self.gf.add_edges_from(e)
                
                
                #karate_club_graph()
        if connectdist=="star":
            n=self.size
            e=[]
            for a in range(n):
                e.append([a,(n+1)%n])
                #dic={}
                #for a in range(self.size):
                #    dic[a]=self.gf.nodes[a][obj]
                #nx.set_node_attributes(te,dic,"obj")                    
                #self.gf=te  
            self.gf.add_edges_from(e)
        if connectdist=="circle":
            n=self.size
            e=[]
            for a in range(n):
                e.append([a,(a+1)%n])
                #dic={}
                #for a in range(self.size):
                #    dic[a]=self.gf.nodes[a][obj]
                #nx.set_node_attributes(te,dic,"obj")                    
                #self.gf=te  
            self.gf.add_edges_from(e)
                        
                
                #karate_club_graph()
        self.agentsid=self.gf.nodes
        for a in self.agentsid:
            self.agents.append(self.getobj(a))
    def setup(self, genway="random"):
        #sets up tastes and assigns the inf stuff
        pref={}
        for a in keys:
            pref[a]=0
        for a in self.gf.nodes():
            dic=pref
            for b in keys:
                dic[b]=rng.random()
            self.getobj(a).define_preferences(dic)
                
        ninf=5
        
        inf=random.sample(self.gf.nodes,ninf)
        for a in inf:
            self.infobj.append(self.getobj(a))
        watchers=self.agentsid
        for a in range(self.size):
            self.ginf.add_node(a,obj=self.getobj(a))
        infdic={}
        for a in inf:
            infdic[a]=[]
        if genway=="random":
            for a in watchers:
                b=random.choice(inf)
                infdic[b].append(a)
                self.ginf.add_edge(b,a)
        if genway=="stricttaste":
            for a in watchers:
                pref=self.getobj(a).preferences
                sco=-100000000000

                nu=0
                for b in range(ninf):
                    be=inf[b]
                    inpref=self.getobj(be).preferences
                    s=getscore(pref,inpref)
                    if sco<s:
                        nu=b
                        sco=s
                infdic[inf[nu]].append(a)
            self.ginf.add_edge(a,inf[nu])
        if genway=="unstricttaste":
            for a in watchers:
                pref=self.getobj(a).preferences
                sco=[]
                for b in range(ninf):
                    be=inf[b]
                    inpref=self.getobj(be).preferences
                    sco.append(getscore(pref,inpref))
                nu=rng.choice(range(ninf),1,sco)
                infdic[inf[nu]].append(a)
            self.ginf.add_edge(a,inf[nu])
        if genway=="double":
            #might not work
            for a in watchers:
                b=random.choice(inf)
                infdic[b].append(a)
                self.ginf.add_edge(b,a)
            for a in watchers:
                pref=self.getobj(a).preferences
                sco=-100000000000
                nu=0
                for b in range(ninf):
                    be=inf[b]
                    inpref=self.getobj(be).preferences
                    s=getscore(pref,inpref)
                    if sco<s:
                        nu=b
                        sco=s
            infdic[inf[nu]].append(a)
            self.ginf.add_edge(a,inf[nu])
        #puts the inf stuff into a usable form
        self.infdic=infdic
        for a in self.infdic.keys():
            self.getobj(a).define_followers(self.infdic[a])

    def friendsof(self,personnr):
        return(list(self.gf[personnr]))
    def getobj(self,personnr):
        return self.gf.nodes[personnr]["obj"]
    def draw(self):
        nx.draw(self.gf)
    def drawi(self):
        nx.draw(self.ginf)
    def addinf(self):
                ####sketch, can be erased
        #choose numinf randomagents as infs
        # generate score for each inf according to taste similarity
        # chose infperag ones according to score
        pass
        #probably output a dic of ags per inf, but also add inf as a trait of ag
        
        

#### AGENTS ####

people_total = [] #list of person objects
games_total = [] #list of game objects
friendship_prob = 0.3
influencer_prob = 0.3
advertising_power = 0.3
standard_decay = -0.3
decay_multiplier =0.2
comparison_budget = 1000

likes = ['singleplayer', 'multiplayer', 'casual', 'replayable', 'rpg']
genres = ['fps', 'puzzle', 'strategy', 'platformer', 'sim']


class Agent:      
    def __init__(self,node_num):
        self.node_num = node_num
        self.friends = []
        self.followers = []
        self.knowngames = {}
        self.preferences = {}
        self.preferences_list=[]
        self.now_playing = 0
        self.time_playing = 0
        self.influencer_status = False



    def define_friends(self, friends_list):
        self.friends = friends_list
        
    def define_followers(self, followers_list):
        self.followers.extend(followers_list)
        self.influencer_status = True
        
    def define_knowngames(self, games_dict):
        self.knowngames = games_dict
    
#    def set_preferences(self,likes:list):
#        self.preferences_list=likes
        

    def define_preferences(self, pref_dict ={}):
        self.preferences = pref_dict
        #else:
         #   if scores:
          #      for i in range(len(scores)):
           #         self.preferences[self.preferences_list[i]]=scores[i]
            #for item in self.preferences_list:
             #   if item not in self.preferences:
              #      self.preferences[item]= 0
        
    def get_friends(self):
        return self.friends
    
    def get_followers(self):
        return self.followers
    
    def get_knowngames(self):
        return self.knowngames
    
    def get_preferences(self):
        return self.preferences
    
    def influence_playing(self,key,prob):
        self.knowngames[key] += prob
    
    def recommend(self):
        for i in self.friends:
            i.influence_playing(self.now_playing,friendship_prob)
        if self.followers:
            for i in self.followers:
                i.influence_playing(self.now_playing,influencer_prob)
        
    def game_infection(self):
        for game in sorted(self.knowngames, key=self.knowngames.get, reverse=True):
            prob=self.knowngames[game] 
            if random.choice([0,1],[1-prob,prob]):
                self.now_playing = game
                self.time_playing +=1
                #return True
                break
    
#    def decay_effect(self):
#        if self.now_playing:
#            disinterest =self.time_playing*self.now_playing
#            self.influence_playing(self.now_playing, disinterest)
   
    
class Game:
#    decay = 0
#    popularity = 0.0
#    budget = 0.0
#    multiplayer = 0.0
#    singleplayer = 0.0
#    mainstream = 0.0
#    target = 0.0 #niche - mainstream
#    team = ["indie","blockbuster"] #optional?
    def __init__(self,name, budget, decay = 0, genre = 0, scores = []):
        self.name = name
        self.budget = budget
        self.decay = decay
        self.genre = genre
        self.scores = scores
        self.effect = advertising_power*self.budget/comparison_budget
        
    def get_popularity(self, people=people_total):
        players = 0
        for i in people:
            if self.name == i.now_playing:
                players += 1
        self.popularity = players/len(people)
        return self.popularity
    
    def get_totalplayers(self, people=people_total):
        players = 0
        for i in people:
            if self.name == i.now_playing:
                players += 1
        return players
    
    def run_add(self, people=people_total):
        for i in people:
            i.influence_playing(self.game, self.effect)
    

    def define_scores(self, keys=likes, scores_list=[], scores_dic={}):
        if scores_dic:
            self.scores = scores_dic
        elif scores_list:
            for i in range(len(scores_list)):
                self.scores[keys[i]]=scores_list[i]
        for item in keys:
            if item not in self.scores:
                self.scores[item] = 0
    
    def set_decay(self, value=standard_decay):
        self.decay = value

    
    
#### CONVERSION ALGORITHM ####
    
class Conversionalgo:
    def __init__(self, step_num=0):
        self.counter = step_num
        self.currentstatus = {}
        
    def implement_influence(self):
        for item in games_total:
            item.run_add()
        for person in people_total:
            person.recommend()
        for person in people_total:
            person.game_infection()
    
    def get_currentstatus(self):
        for item in games_total:
            self.currentstatus[str(item)] = item.get_totalplayers()
        
    def get_deltas(self):
        pass
    #more?

#### SIMULATION MANAGER ####

#https://www.tutorialspoint.com/python/python_classes_objects.htm
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/

class Simumanager:
    'class that manages the simulation & works with timestamps'
    timeStamp = 0   #accessable from in/outside the class
        
    def __init__(self):
        Simumanager.timeStamp = 0 #init the timestamp to 0 for a new simulation



    def loadsimu(self, timestamp, datafile):
        Simumanager.timeStamp = timestamp

    def networkinit(self):      #Setup
        net = Network()
        net.generate()

    def networkfillup(self):
        self.net.setup()
        self.net.draw()
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
    def savenetwork(self):
        pass
    def savecurrenttimestamp(self):
        pass
    
    
#### PLOTTER ####
        
class plotter:
    def setupplot(self):
        pass
    def drawnodes(self):
        pass
    def drawedges(node, depth):     #node: person & influencer, depth: how many levels of friends of friends of frieds i.e.
        pass
    def update(self):
        pass
    def exportplot(self):
        pass

