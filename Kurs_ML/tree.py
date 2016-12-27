from sklearn import tree

X = []
Y = []
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

prediction = clf.predict()