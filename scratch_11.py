#line chart
import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.pyplot.yticks
##xrange=[.2,.45]
#yrange=[0,1,0.2]
#plt.style.use('classic')
fig, ax = plt.subplots()
axes=plt.axes()
axes.set_ylim([0,0.6])
#plt.axis=([0,0.45,0.2,0.6])
#x_data=[0.53,0.25,0.25,0.1,0.1,0.1]
#y_data=[0.53,0.62,0.58,0.51,0.5,0.61]
plt.grid(True)
plt.yticks(np.arange(0.0,1.25,0.25))
#plt.yticks(np.arange(0, 11, 1))

plt.title('200 Documents')
plt.xlabel('min sup')
plt.ylabel('F-score')
#plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.61,0.59,0.56,0.5,0.61],color='r',marker='o',label='WFUP_AC')
#plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.52,0.2,0.2,0.1,0.1,0.1],color='b',marker='o',label="MC")
#

#500D
#plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.57,0.56,0.57,0.56,0.565,0.6],color='r',marker='o',label='WFUP_AC')
#plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.4,0.39,0.41,0.29,0.18,0.15],color='b',marker='o',label="MC")
#plt.legend(bbox_to_anchor=(0.8, 1), loc=2, borderaxespad=0.)

#200 D

plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.67,0.68,0.61,0.62,0.64],color='r',marker='o',label='WFUP_AC')
plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.87,0.86,0.45,0.76,0.74],color='b',marker='o',label="MC")

#100D
#plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.85,0.95,0.92,0.75,0.76,0.77],color='r',marker='o',label='WFUP_AC')
#plt.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.49,0.48,0.37,0.37,0.25,0.39],color='b',marker='o',label="MC")
plt.legend(loc='upper right')

#plt.xlabel('min_sup')
#plt.ylabel('F_Score')



#plt.xlim(xrange)
#plt.ylim(yrange)
plt.show()
