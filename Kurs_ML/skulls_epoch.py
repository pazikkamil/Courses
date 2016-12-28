import numpy as np
import pandas
from sklearn.neighbors import KNeighborsClassifier

# Remove the column containing the target name since it doesn't contain numeric values.
# Also remove the column that contains the row number
# axis=1 means we are removing columns instead of rows.
# Function takes in a pandas array and column numbers and returns a numpy array without
# the stated columns


def removeColumns(pandasArray, *column):
    return pandasArray.drop(pandasArray.columns[[column]], axis=1).values

my_data = pandas.read_csv("https://ibm.box.com/shared/static/exmvrr3eic0u6ete9zev5crwpjs0s295.csv", delimiter=",")

print(type(my_data))
# <class 'pandas.core.frame.DataFrame'>

