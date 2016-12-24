from sklearn.neighbors import KNeighborsClassifier
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

iris = load_iris()

# check what we have
iris.keys()
iris['DESCR'][:193]

""" interesting data """
# iris['target_names']
# iris['feature_names']
# iris['data']
# iris['data'].shape # rows x columns


iris['data'][:4]
# show rows till 4-th


# check shape
iris['target'].shape

# it shuffles data using pseudo random num generator before spliting
X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)

# test_size - decides how huge is sample
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

X_new = np.array([[5, 2.9, 1, 0.2]])
X_new.shape

# making predictions

prediction = knn.predict(X_new)
prediction

iris['target_names'][prediction]