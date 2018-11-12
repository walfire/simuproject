# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:47:45 2018

@author: chris
"""

import networkx as nx
class test(object):
    def __init__(self, na, bo):
        self.na=na
        self.bo=bo
a=test("Fridolin",10)
g=nx.Graph()
g.add_node(1,ob=a)
g.nodes
g.add_edge(1,3)
g.add_edge(1,7)