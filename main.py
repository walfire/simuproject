#### SIMU PROJECT ####

###Libraries###
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx 
import numpy.random as rng
import pandas as pd
import random


#### CLASSES ####

#### NETWORK STRUCTURE ####
n = 500
keys=["complex" , "friendly" , "meaning","polish" , "multi", "action", "difficulty", "abstract"]

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
        self.ginf=nx.Graph()
        self.infperag=1
        self.numinf=10
        self.infdic={}
        self.infobj=[]
        
    def generate(self,meanfriends=5, sdfriends=5, frienddist="uni",connectdist="watstro"):
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
        elif connectdist=="randomunif":
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
        elif connectdist=="randomunif2":
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
        elif connectdist=="prederd":
            n=self.size
            k=10/(n-1)
            te=nx.gnp_random_graph(n,k)
            self.gf.add_edges_from(te.edges)
        elif connectdist=="watstro":
            n=self.size
            p=0.05
            k=10
            te=nx.connected_watts_strogatz_graph(n,k,p,100) 
            self.gf.add_edges_from(te.edges)
        elif connectdist=="bara":
            n=self.size
            p=0.05
            k=5
            te=nx.barabasi_albert_graph(n,k)
            self.gf.add_edges_from(te.edges)
        elif connectdist=="pow":
            n=self.size
            #k=min(n/10,5)
            k=4
            p=0.05
            te=nx.powerlaw_cluster_graph(n,k,p) 
            self.gf.add_edges_from(te.edges)
        elif connectdist=="full":
            n=self.size
            e=[]
            for a in range(n-1):
                for b in range(a+1,n):
                    e.append(set([a,b]))
            self.gf.add_edges_from(e)
                
                
                #karate_club_graph()
        elif connectdist=="star":
            n=self.size
            e=[]
            for a in range(n):
                e.append([a,(n+1)%n])
            self.gf.add_edges_from(e)
        elif connectdist=="circle":
            n=self.size
            e=[]
            for a in range(n):
                e.append([a,(a+1)%n]) 
            self.gf.add_edges_from(e)
                #karate_club_graph()
                
        else:
            raise Exception("ERROR: UNVALID GENERATE KEY")

        self.agentsid=self.gf.nodes
        for a in self.agentsid:
            self.agents.append(self.getobj(a))
            self.getobj(a).define_friends(self.friendsof(a))
            
            
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
                infdic[inf[nu]].append(self.getobj(a)) #attention check
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
            for b in self.infdic[a]:
                self.getobj(b).influencer=self.getobj(a)
                
    def friendsof(self,personnr):
        return(list(self.gf[personnr]))
        
    def getobj(self,personnr):
        return self.gf.nodes[personnr]["obj"]
    
    def draw(self):
        ax=plt.gca()
        ax.clear()
        fig = plt.gcf()
        #fig.set_size_inches(13,20)#    set dimension of window
        nx.draw(self.gf,node_size=100,node_color="red")
        
    def drawi(self):
        ax=plt.gca()
        ax.clear()
        fig = plt.gcf()
        nx.draw(self.ginf)
    def addinf(self):
                ####sketch, can be erased
        #choose numinf randomagents as infs
        # generate score for each inf according to taste similarity
        # chose infperag ones according to score
        pass
        #probably output a dic of ags per inf, but also add inf as a trait of ag
    def niceplot(self):
        ax=plt.gca()
        ax.clear()
        fig = plt.gcf()
        toplot=nx.Graph()
        for a in self.agents:
            if a.node_num in self.inf:
                eee="d"
                aaa=100+10*a.time_playing
            else:
                eee="d"
                aaa=30+5*a.time_playing
            toplot.add_node(a.node_num,col=a.now_playing,size=1,shape=eee)
        toplot.add_edges_from(self.gf.edges,col="k",wei=2)
        #for aa in range(len(self.inf)):
         #   a=self.inf[aa]
          #  for b in list(self.ginf[a]):
           #     toplot.add_edge(a,b,col=getcol(aa),wei=5)
        toplot.add_edges_from(self.ginf.edges,col="r",wei=1)
        
        edges=toplot.edges
        nodes=toplot.nodes
        colors = [toplot[u][v]['col'] for u,v in edges]
        wei = [toplot[u][v]['wei'] for u,v in edges]
        coln=[toplot.nodes[u]["col"] for u in nodes]
        size=[toplot.nodes[u]["size"] for u in nodes]
        shape=[toplot.nodes[u]["shape"] for u in nodes]
        #print(colors)
        nx.draw_networkx(toplot, nodes=nodes, node_color= coln, node_size=size, 
                #node_shape=shape, 
                edges=edges, edge_color=colors, 
                width=wei
                )
def getcol(a):
    col=["g","b","y","m","r"]
    return col[a]

#### AGENTS ####
people_total = [] #list of person objects
games_total = [] #list of game objects
games_dict = {0:0} #dictionary of str(game objects)
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
        self.node_num = node_num          #ID of agent
        self.friends = []
        self.followers = []
        self.influencer = 0
        self.knowngames = {}
        self.preferences = {}
        self.preferences_list=[]
        self.now_playing = 0
        self.time_playing = 0
        self.influencer_status = False
        people_total.append(self)
        
    def __str__(self):
        return self.node_num

    def define_friends(self, friends_list):
        self.friends = friends_list
        
    def define_followers(self, followers_list):
        self.followers.extend(followers_list)
        self.influencer_status = True
        
    def define_knowngames(self, games_dict):
        self.knowngames = games_dict.copy()
    
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
    
    def decay_playing(self):
        #if statt {0:0}
        self.knowngames[str(self.now_playing)] += standard_decay
    
    def recommend(self):
        for i in self.friends:
            print(i)
            newi = i #to be replaced
            newi.influence_playing(self.now_playing,friendship_prob)
        if self.followers:
            for j in self.followers:
                j.influence_playing(self.now_playing,influencer_prob)
        
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
    game_num = 0
    def __init__(self, budget, name = game_num, game_id= game_num, decay = 0, genre = 0, scores = []):
        self.name = name
        self.budget = budget
        self.decay = decay
        self.genre = genre
        self.scores = scores
        self.effect = advertising_power*self.budget/comparison_budget
        self.game_id = game_id
        games_total.append(self)
        games_dict[str(self)]=0
        Game.game_num += 1
        
    def __str__(self):
        return str(self.name)
        
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
        
    # def implement_influence(self):        #commented out because now in simumanager
    #     for item in games_total:
    #         item.run_add()
    #     for person in people_total:
    #         person.recommend()              #ev in game class
    #     for person in people_total:
    #         person.game_infection()
    
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
    timestamp = 0   #accessable from in/outside the class

    def __init__(self):
        Simumanager.timestamp = 0 #init the timestamp to 0 for a new simulation

    def loadsimu(self, timestamp, datafile):
        Simumanager.timestamp = timestamp

    def addgames(self,gamesnumber=5, budget="random"):  #create n instances of games, which automatically get added in games_total list
        if budget == "random":
            budgetamount = random.random()
            for i in range(0,gamesnumber):
                Game(budgetamount)
        else:                                           #open for extension for non random assignment of budget
            raise Exception("ERROR: INVALID BUDGET PARAMETER INPUT")

    def networkinit(self,agentsnumber=500,influassignment="random"):      #creates n agents (500 as preset), assigns preferences,
        net = Network(size=agentsnumber)
        net.generate()   # using watstro simulation as preset
        net.setup(influassignment)  #random, stricttaste, unstricttaste, double keys for influencer init and assignment

    def drawnetwork(self,type="agents"):
        if type == "agents":
            self.net.draw()
        if type == "influencers":
            self.net.drawi()
        if type == "agents_influencers":
            self.net.niceplot()
        else:
            raise Exception("Error: INVALID TYPE PARAMETER INPUT")

    def stateofknowngame(self):     #1 Timestamp
        pass
    
    def adround(self):
        for item in games_total:
            if item is not "Null_Game":         #there wont be an AD for a Non Game
                item.run_add

    def influfriendround(self):
        for person in people_total:
            person.recommend()          #includes friend influence over other friends, and influencers influence

    def conversion(self):               #decides which game gets played
        for person in people_total:
            person.game_infection()

    def exporttimestamp(self):
        pass

    def get_agents(self):
        pass

    def get_games(self):
        pass

    def decay(self):
        pass

    def nextstep(self):             #increases timestamp of simulation by 1
        self.timestamp +=1

##### DATA MANAGER ####

class Datamanager:          #call it after the network creation, to instantiate a pandas matrix that has the information
                            #about all the agents at timestamp = 0
    def __init__(self):
        self.columns = ["timestamp", "agent ID", "isinfluencer", "current played game", "how long been playing current game", "# friends playing the same", "does influencer play the same"]
        
        if games_total:                 #appends to the index list the names of the played games list
            for game in games_total:
                if game.name != "Null_Game":
                    self.columns.append("game " + str(game.name) + " preference %")     
        self.listofagents = []
        self.table = pd.DataFrame(data = self.listofagents, columns = self.columns)

    def get_table(self):
        print (self.table)

    def update_table(self):
        for person in people_total:
            agent = []
            agent.append(Simumanager.timestamp)
            agent.append(person.node_num)
            agent.append(person.influencer_status)
            agent.append(person.now_playing)
            agent.append(person.time_playing)       # check on thisi
            agent.append(0) #nr friends playing the same game
            agent.append(0) #is influ playing the same?
            for game in games_total:        #TO BE CHECKED IF THE ORDER IS THE SAME OF THE ONE IN THE PANDA DATAFRAME
                if game.name != "Null_Game":
                   # agent.append(agent.preferences[game.name])
                   agent.append("placeholder")
            self.listofagents.append(agent)
            
        self.table = pd.DataFrame(data = self.listofagents, columns = self.columns)
            
    def export_table(self):
        writer = pd.ExcelWriter('Simulation.xlsx', engine='xlsxwriter')
        self.table.to_excel(writer, sheet_name='Sim')
        writer.save()
        
    def createtable(self):
        pass
    def savecurrenttimestamp(self):
        pass


#sim = Simumanager()
#sim.addgames()
#sim.networkinit()
#sim.drawnetwork()
#data = Datamanager()
#data.get_table()
#data.export_table()
       
        
def main(): 
    print ("START OF SIMULATION \n")
    sim = Simumanager()
    sim.addgames()
    net = Network()
    net.generate()
    net.setup()
    data = Datamanager()
    rounds = int(input("How many rounds of simulation?      "))
    for i in range(rounds):
        print("Timestamp " + str(sim.timestamp))
        
        sim.adround()               #influence of ads, influencers and friends & conversion calculated
        sim.influfriendround()
        sim.conversion()
        
        data.update_table()         #export values in the table
        data.get_table()
        data.export_table()
        
        
        net.draw()                  #draw plot
        
        
        if i < (rounds-1):
            input("Proceed with next step?: ")
            sim.nextstep()
        else:
            print("Simulation finished.")
        
    
if __name__ == "__main__":
    main()

##### PLOTTER ####
#        
#class plotter:
#    def setupplot():
#        pass
#    def drawnodes():
#        pass
#    def drawedges(node, depth):     #node: person & influencer, depth: how many levels of friends of friends of frieds i.e.
#        pass
#    def update():
#        pass
#    def exportplot():
#        pass