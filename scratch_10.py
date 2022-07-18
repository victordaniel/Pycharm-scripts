import networkx as nx
import matplotlib.pyplot as plt
#G=nx.read_edgelist("D:/facebook_combined.edges")
#nx.draw(G)

import networkx as nx
import pandas as pd

df = pd.read_csv('C:/victor/ML/papers/OSN ANOMOLY/myfolder/paper/papers for project/New folder/mywork/presentation/anomoulous node/facebookdata/TwitterFriends/data.csv')
#Graphtype = nx.Graph()
#G = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)



plt.show()
print(len(G.nodes()))
deg=nx.degree(G)
deg=list(deg)

print(deg)
