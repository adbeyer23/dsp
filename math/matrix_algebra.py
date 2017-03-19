# Matrix Algebra

import numpy as np
A = np.matrix([[1,2,3], [2,7,4]])
B = np.matrix([[1, -1], [0,1]])
C = np.matrix([[5,-1], [9,1], [6,0]])
D = np.matrix([[3, -2,-1], [1,2,3]])
u = np.matrix([[6,2,-3,5]])
v = np.matrix([[3,5,-1,4]])
w = np.matrix([[1], [8], [0], [5]])

onepointone = A.shape
onepointtwo = B.shape
onepointthree = C.shape
onepointfour = D.shape
onepointfive =u.shape
onepointsix = w.shape
twopointone = np.add(u,v)
twopointtwo = u - v
twopointthree = 6 * u
twopointfour = np.sum(np.multiply(u,v))
twopointfive = np.linalg.norm(u)
threepointone = "Undefined"
threepointtwo = A - C.T
threepointthree = C.T + (3 * D)
threepointfour = B*A
threepointfive = "Undefined"
threepointsix = "Undefined"
threepointseven = C*B
threepointeight = np.linalg.matrix_power(B,4)
threepointnine = A * A.T
threepointten = D.T * D

'''
Answers
1.1 2x3  
1.2 2x2  
1.3 3x2  
1.4 2x3  
2.1 [9,7, -4, 9]  
2.2 [3,-3,-2,1]  
2.3 [36,12,-18,30]  
2.4 51  
2.5 8.602  
3.1 Undefined  
3.2 [-4, -7, -3]  
    [3,   6,  4]  
      
3.3 [14, 3, 3]  
    [2,  7, 9]  
3.4 [-1, -5, -1]  
    [2,   7, -4]
3.5 Undefined
3.6 Undefined
3.7 [5,-6]
    [9,-8]
    [6,-6]
3.8 [1, -4]
    [0, 1 ]
3.9 [14, 28]
    [28, 69]
3.10 [10, -4, 0]
     [-4, 8,  8]
     [0,  8, 10]
'''
