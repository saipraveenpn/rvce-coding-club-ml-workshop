import numpy as np 
a = np.array([[1, 2], [3, 4]]) 

print (a.shape)

a = np.array([1, 2, 3,4,5], ndmin = 2) 

a = np.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 

#Return the min element
print(np.min(a))

#To find the max element in each column
print(np.max(a , axis=0))

#To find the max element in each row
print(np.max(a , axis=1))
