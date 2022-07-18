from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
a=np.array([1,0,1])
b=np.array([0,1,1])
c=np.array([1,1,1])
d=np.array([1,1,1])
e=np.array([1,0,0])
aa=a.reshape(1,-1)
bb=b.reshape(1,-1)
cc=c.reshape(1,-1)
dd=d.reshape(1,-1)
ee=e.reshape(1,-1)
print(cosine_similarity(cc,dd))
print(cosine_similarity(ee,dd))
ans=cosine_similarity(bb,ee)
print("ans={}".format(ans))



