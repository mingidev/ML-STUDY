import numpy as np
import matplotlib.pyplot as plt

def binary_step_activate_function(x):
    return np.tanh(x)
    
x = np.arange(-10, 10, 0.1)
y = binary_step_activate_function(x)

plt.plot(x,y)
plt.show()
