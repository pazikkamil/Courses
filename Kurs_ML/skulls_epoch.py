import numpy as np
import pandas
from sklearn.neighbors import KNeighborsClassifier


my_data = pandas.read_csv("https://ibm.box.com/shared/static/exmvrr3eic0u6ete9zev5crwpjs0s295.csv", delimiter=",")