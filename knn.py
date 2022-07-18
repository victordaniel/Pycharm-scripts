import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
import seaborn as sns
iris = pd.read_csv("C:/Users\christy\Desktop\.ipynb_checkpoints\iris.csv", index_col=0)
print(iris.head())
sns.pairplot(iris, hue="variety");
knn1 = KNeighborsClassifier()
X_train = iris.drop("variety", axis=1).values
y_train = iris.variety.values
print(cross_val_score(knn1, X_train, y_train, cv=5))

#gridsearch to find best
select_params = {"n_neighbors": range(1, 11),
                 "weights": ["uniform", "distance"],
                 "metric": ["euclidean", "manhattan", "chebyshev", "minkowski"]}
knn2 = KNeighborsClassifier()
grid_knn1 = GridSearchCV(knn2, select_params, cv=5)

print(grid_knn1.fit(X_train, y_train))