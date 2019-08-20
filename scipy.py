from scipy import linalg
A=numpy.array([[2,3],[3,4]]) # 2x+3y=7 and 3x+4y=10
B=numpy.array([[7],[10]])
linalg.solve(A,B) # x = 2 , y = 1
linalg.det(A)
