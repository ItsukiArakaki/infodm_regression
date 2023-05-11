import matplotlib.pyplot as plt
import math
import numpy as np
#def true_function(x):
#    y = x + 1
#    return y
def true_function(x):
    y = np.sin((np.pi * x * 0.8)) * 10
    return y

#num = np.array([0.])
#print(true_function(num))
x = np.arange(-1, 2)
y = true_function(x)
plt.plot(x, y)
plt.show()