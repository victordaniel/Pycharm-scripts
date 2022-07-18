import networkx as nx
import matplotlib.pyplot as plt
import scipy.spatial.distance
import scipy
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
from scipy.spatial import distance_matrix

G=nx.Graph()
G.add_node(1, weight = 2)
G.add_node(2, weight = 3)
G.add_edge(1,2, flux = 5)
G.add_edge(2,4)

H=nx.Graph()
H.add_node(1, weight = 4)
H.add_edge(1,2, flux = 10)
H.add_edge(1,3)

F = nx.compose(G,H)
print(len(F.nodes()))
nx.draw(F,with_labels=True)
plt.show()


F = nx.compose(G , H)
print("len of G ={}".format(len(G.nodes())))
anomaly=[]

for i in F.nodes():
    dist=[]
    ego = nx.ego_graph(F, i)
    len_ego=len(ego)
    print(str(i) + "=" + str(len(ego.nodes())))
    adj_mat = nx.to_numpy_matrix(ego)
    print((adj_mat))

    # neighbors of ego
    # neigh=[n for n in ego.neighbors(i)]
    neig = (list(ego.neighbors(i)))
    print(neig)
    neig.append(i)

    # arrange neighbors in order
    neig.sort()
    print("neig=" + str(neig))

    # find the position of ego in the neighbors
    ind = neig.index(i)
    print("index  of {}in neig is {} ".format(i, ind))

    # extract index row into row
    row = adj_mat[ind]
    print("row=" + str(row))
    print(type(row))

    for  j in adj_mat:
        print("j={}".format(j))

    # compare key row with every other row and find distance
    count_of_1 = 0
    for j in adj_mat:

        # dist.append\
        print("comparing  {} and  {}".format(adj_mat[ind],j))
        #d=(scipy.spatial.distance.cosine(adj_mat[ind], j))
        d=cosine_similarity(adj_mat[ind],j)
        print("d={}".format(d))
        if (d >= 0.5):
            count_of_1 = count_of_1 + 1
        print("count_of_1={}".format(count_of_1))

    count_of_1=count_of_1-1

    len_ego=len_ego*0.5

    #calculate anomaly
    if(count_of_1 <= len_ego):
        print("{} is an anaomaly,because count-of-1= {}and ego_nodes={} ".format(i,count_of_1,len_ego))
        anomaly.append(i)
print("Total nodes= {}".format(len(G.nodes())))
print("Anomalous nodes= {}".format(len(anomaly)))
print("anomalous nodes are{}".format(anomaly))
