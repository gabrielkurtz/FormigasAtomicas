import matplotlib.pyplot as plt
import networkx as nx
import random

def plot( path ):
    G = nx.DiGraph()
    list = []
    for i in range( len( path ) - 1):
        # print( "(" + str ( path(i) )  , str ( path(i+1) ),  ")" , " " )
        list.append( ( path[i] , path[i + 1] ) )
    G.add_edges_from(list)
    pos = nx.spring_layout(G)
    nx.draw_networkx_labels(G, pos)
    black_edges = [edge for edge in G.edges()]
    values = [random.uniform(0, 1) for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
    plt.show()