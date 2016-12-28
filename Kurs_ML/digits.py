from sklearn.datasets import load_digits
from sklearn import svm

digits = load_digits()

print(digits.keys())
print(digits.DESCR)

print(digits.data.shape)
print(digits.target.shape)


max([ max(i) for i in digits.data])


X = digits.data
y = digits.target


clf = svm.SVC(gamma=0.001, C=100)
clf.fit(X, y)

print('Prediction:'), clf.predict(digits.data[-1])
print('Actual:'), y[-1]