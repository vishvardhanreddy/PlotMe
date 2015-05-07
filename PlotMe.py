'''
Created on Nov 26, 2014

@author: vvaka
'''
 
import networkx as nx


def main():
   
    G=nx.Graph('fig.png')
    G.add_node("spam")
    G.add_edge(1,2)
    print(G.nodes())
    [1, 2, 'spam']
    print(G.edges())
    [(1, 2)]