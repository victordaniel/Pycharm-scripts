#line chart
import matplotlib.pyplot as plt
import numpy as np


axes=plt.axes()
axes.set_ylim([0,0.6])
#plt.axis=([0,0.45,0.2,0.6])
#x_data=[0.53,0.25,0.25,0.1,0.1,0.1]
#y_data=[0.53,0.62,0.58,0.51,0.5,0.61]
plt.grid(True)
plt.yticks(np.arange(0.0,0.8,0.2))
#plt.yticks(np.arange(0, 11, 1))


plt.title('comparison of 100 Documents')
plt.xlabel('min sup')
plt.ylabel('F-score')
plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.5,0.59,0.57,0.51,0.52],color='r',marker='o',label='WFUP_AC')
plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.4,0.41,0.41,0.43,0.44,0.21],color='b',marker='o',label="Maximum Capturing")
plt.legend(loc="lower right")

plt.show()