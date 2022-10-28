import numpy as np

# define your X and Y as NumPy Arrays
X = np.array([1,3,5])
Y = np.array([4.8,12.4,15.5])

# np.polyfit function does a 1-dimensional Polynomial fitting
# and the np.poly1d function converts the polynomial coefficents 
# into a polynomial object that can be evaluated

p = np.poly1d(np.polyfit(X,Y,1))
print(p)
