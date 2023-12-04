import numpy as np
x = np.array([1,2,3,4])
print("Original array : ",x)
print("Test if none of the elements of the said array is zero: ",np.all(x))
x = np.array([0,1,2,3])
print("Original array : ",x)
print("Test if none of the elements of the said array is zero: ",np.all(x))