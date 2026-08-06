import matplotlib.pyplot as plt
import numpy as np
phase = ['FS','RA','DESIGN','CODING','INTEGTAION','MAINTAINAENCE']
cost= [1.9,1.8,3.3,1.4,2.1,4.5]
plt.pie(cost, labels=phase, autopct='%1.1f%%')
plt.title('Cost Distribution')
plt.axis('equal')
plt.legend(title='Phase', loc='best')
plt.show()