import numpy as np
from numpy import *
list = np.arange(25)

print("Original Array")
print(list)

y_mean = np.mean(list)
print("\nMean: ", y_mean)

y_std = np.std(list)
print("\nStandard deviation: ", y_std)

y_var = np.var(list)
print("\nVariance:", y_var)

