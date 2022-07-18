import networkx as nx
import matplotlib.pyplot as plt
import scipy.spatial.distance
import scipy
from sklearn.metrics.pairwise import cosine_similarity




p = nx.read_edgelist("C:/victor/ML/papers/OSN ANOMOLY/myfolder/paper/papers for project/New folder/mywork/presentation/anomoulous node/facebookdata/facebook.tar/facebook/107.edges")
q = nx.read_edgelist("C:/victor/ML/papers/OSN ANOMOLY/myfolder/paper/papers for project/New folder/mywork/presentation/anomoulous node/facebookdata/facebook.tar/facebook/0.edges")
print("this is demo")
#nx.draw(p)
#plt.show()
print("len of p ={}".format(len(p.nodes())))
print("len of q ={}".format(len(q.nodes())))

#F = nx.compose(p , q)
F=nx.read_edgelist("D:/facebook_combined.edges")
print("len of G ={}".format(len(F.nodes())))



anomaly=[]

for i in F.nodes():

    dist=[]
    deg=nx.degree(F,i)
    if(deg<=15):
        continue
    ego = nx.ego_graph(F, i)
    deg=nx.degree(ego,i)
    if(deg<=15):
        continue
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
        if (d >= 0.4):
            count_of_1 = count_of_1 + 1
        print("count_of_1={}".format(count_of_1))

    count_of_1=count_of_1-1

    len_ego=len_ego*0.20

    #calculate anomaly
    if(count_of_1 <= len_ego):
        print("{} is an anaomaly,because count-of-1= {}and ego_nodes={} ".format(i,count_of_1,len_ego))
        anomaly.append(i)
print("Total nodes= {}".format(len(F.nodes())))
print("Anomalous nodes= {}".format(len(anomaly)))
print("anomalous nodes are{}".format(anomaly))
