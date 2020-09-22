#1/usr/bin/python
#-*-coding: utf-8 -*-
#from pylab import figure
import pylab
import networkx as nx
G=nx,read_weighted_edgelist('soda.txt',create_using=nx.Graph() )
nx.draw(G, with_labels= True)