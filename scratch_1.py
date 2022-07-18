import numpy as np
from scipy.sparse import csr_matrix
 # Based on Example from paper
rows = [0,0,0,0,1,1,1,2,2,2,3,3,3,3,4,4,4,4,
            5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,8,8,8,
            9,9,9,9,10,10,10,10,11,11,11,11,
            12,12,12,12,12,13]
cols = [1,4,5,6,0,5,2,1,5,3,2,4,5,6,0,3,5,6,
            0,1,2,3,4,4,0,3,7,11,10,6,11,12,8,7,
            12,9,8,12,10,13,9,12,11,6,7,12,10,6,
            7,8,9,10,11,9]
data = np.ones(len(rows))
G =csr_matrix((data,(rows,cols)),shape=(14,14))
print(type(G))
#print (G)