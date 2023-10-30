#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from numpy.polynomial import Polynomial
P=Polynomial([1,2,0,3])
print(P)
Q=P*P
print(Q)
print("P(2)=",P(2))
print("Q(2)=",Q(2))


# Question1:


import numpy as np
from numpy.polynomial import Polynomial

def base_lagrange(X, i):
    n = len(X)
    result = Polynomial([1.0])

    for j in range(n):
        if j != i:
            term = Polynomial([-X[j], 1]) / (X[i] - X[j])
            result *= term
    return result

X = np.array([]) 
i = 2 
polynomial = base_lagrange(X, i)
print("Polynôme de la base de Lagrange L", i, "(x) :", polynomial)


# Question2:


import numpy as np
from numpy.polynomial import Polynomial

def base_lagrange(X, i):
    n = len(X)
    result = Polynomial([1.0])

    for j in range(n):
        if j != i:
            term = Polynomial([-X[j], 1]) / (X[i] - X[j])
            result *= term  
    return result

def polynome_lagrange(X, Y):
    n = len(X)
    result = Polynomial([0.0])

    for i in range(n):
        term = base_lagrange(X, i) * Y[i]
        result += term
    return result

X = np.array([]) 
Y = np.array([])  

polynomial = polynome_lagrange(X, Y)
print("Polynôme d'interpolation P(x) :", polynomial)


# Question3:


import numpy as np
from numpy.polynomial import Polynomial

def polynome_lagrange(X, Y):
    n = len(X)
    result = Polynomial([0.0])

    for i in range(n):
        term = base_lagrange(X, i) * Y[i]
        result += term
    return result

X = np.array([-1, 0, 1])
Y = np.array([2, 1, -1])

polynomial = polynome_lagrange(X, Y)
print("Polynôme d'interpolation P(x) :", polynomial)







