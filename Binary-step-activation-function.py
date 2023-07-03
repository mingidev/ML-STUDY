import numpy as np
import matplotlib.pyplot as plt

def binary_step_activate_function(x):
    y = x > 0
    return y.astype(np.int)
    
x = np.arange(-3, 3, 0.1)
y = binary_step_activate_function(x)

plt.plot(x,y)
plt.show()
