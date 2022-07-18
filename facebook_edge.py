print("Praise the lord")
import networkx as nx
import matplotlib.pyplot as plt
G=nx.read_edgelist("C:/victor/ML/papers/OSN ANOMOLY/myfolder/paper/papers for project/New folder/mywork/presentation/anomoulous node/facebookdata/facebook.tar/facebook/348.edges")
#print(G)
#plt.show()
print(len(G.nodes()))
deg=nx.degree(G)
deg=list(deg)

#print(deg)

adj_mat = nx.to_numpy_matrix(G)
print(adj_mat)
