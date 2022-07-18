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

plt.show()
anomaly=[]

for i in F.nodes():
    dist=[]
    ego=nx.ego_graph(F,i)
    x=i-1
    print("x="+str(x))
    print(type(ego))
    #construct diagonal matrix
    print(str(i)+"="+str(len(ego.nodes())))
    adj_mat=nx.to_numpy_matrix(ego)
    print((adj_mat))
    #nx.draw(ego,with_labels=True)
    #plt.show()
    #print((am[:(x-1)]))
    #x=am[i-1]
    print('-----')
    #print(x)
    print(" end loop")

    #neighbors of ego
    #neigh=[n for n in ego.neighbors(i)]
    neig=(list(ego.neighbors(i)))
    print(neig)
    neig.append(i)



    #arrange neighbors in order
    neig.sort()
    print("neig="+str(neig))

    #find the position of ego in the neighbors
    ind=neig.index(i)
    print("index  of {}in neig is {} ".format(i,ind))

    #extract index row into row
    row=adj_mat[ind]
    print("row="+str(row))
    print(type(row))


    #compare key row with every other row and find distance
    #np.apply_along_axis(myfunction, axis=1, arr=mymatrix)

    for j in adj_mat:
        count_of_1=0
       # dist.append\
        d=(scipy.spatial.distance.cosine(adj_mat[0,:], j))
        if(d>=0.5):
            count_of_1=count_of_1+1
        print("d={}".format(d))
        print("dist="+str(dist))
        #filter_dist = list(map(lambda y : 1 if y >= 0.5 else 0,dist))
        #count_of_1=filter_dist.count(1.0)

        print("count="+str(count_of_1))
        count_of_1=count_of_1-1
        l=len(dist)
        print("len="+str(l))
        #l=l/2
        l=l*0.3

    if(count_of_1<l):
        anomaly.append(i)
        print("{}is anomalous".format(i))
for i in anomaly:
    print("{}is anomalous".format(i))







