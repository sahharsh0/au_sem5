import matplotlib.pyplot as plt
import numpy as np
y=np.array([2,4,6,8,10])
plt.pie(y, labels=['A', 'B', 'C', 'D', 'E'], autopct='%1.1f%%')
plt.show()