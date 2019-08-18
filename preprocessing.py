import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Importing the dataset

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#Replacing missing values
imputer = SimpleImputer(missing_values = np.nan , strategy = 'mean')
X[:, 1:3] = imputer.fit_transform(X[:, 1:3])

#Rescaling

#from sklearn.preprocessing import MinMaxScaler
#
#data = [[-1, 2], [-0.5, 6], [0, 5], [1, 15]]
#scaler = MinMaxScaler((1,15))
#scaler.fit(data)
#print(scaler.transform(data))

#Standardising

#from sklearn.preprocessing import StandardScaler
#
#data = [[0, 0], [0, 0], [1, 1], [1, 1]]
#scaler = StandardScaler()
#print(scaler.fit(data))
#print(scaler.mean_)
#print(scaler.transform(data))

#Binariser

#from sklearn.preprocessing import Binarizer
#X = [[ 1., -1.,  2.],
#     [ 2.,  0.,  0.],
#     [ 0.,  1., -1.]]
#y = Binarizer( threshold=1).fit_transform(X) 



#Label Encoder

#from sklearn.preprocessing import LabelEncoder
#le = LabelEncoder()
#print(le.fit_transform(X[:,0]))
#X[:,0] = le.fit_transform(X[:,0])

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
