import sklearn
from sklearn import datasets

import matplotlib.pyplot as plt

import pandas as pd
from sklearn.cluster import KMeans
iris = datasets.load_iris()

#print(type(iris))#
#print(iris.values)#
#print(iris.keys)#
#X = iris.data[:, :2]
#y = iris.target
#print(iris.data)#
X = iris.data[:, :2]
y = iris.target
#print(X)#
#print(y)#
plt.scatter(X[:,0], X[:,1],c=y)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()

#kmeans library call
kmeans = KMeans(n_clusters=3, random_state=10)
pred_label=kmeans.fit_predict(X)

print(kmeans.labels_)
print("\n")
print("hello")
print(kmeans.cluster_centers_)
#plt.subplots(1,2,figsize=(10,10))
plt.subplot(1,2,1)
plt.scatter(X[:,0],X[:,1],c=y)
plt.subplot(1,2,2)
plt.scatter(X[:,0],X[:,1],c=pred_label)
plt.show()

