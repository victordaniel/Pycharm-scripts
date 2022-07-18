import matplotlib.pyplot as plt
#plt.subplots(4)

fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
#ax1=fig.add_subplot(2,1,1)
ax1.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.67,0.68,0.61,0.62,0.64],color='r',marker='o',label='WFUP_AC')
ax1.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.87,0.86,0.45,0.76,0.74],color='b',marker='o',label="MC")
plt.title("1000 Documents")

#ax2=fig.add_subplot(2, 1, 2)
ax2.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.67,0.68,0.61,0.62,0.64],color='r',marker='o',label='WFUP_AC')
ax2.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.87,0.86,0.45,0.76,0.74],color='b',marker='o',label="MC")

#ax3=fig.add_subplot(2,2,1 )
ax3.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.67,0.68,0.61,0.62,0.64],color='r',marker='o',label='WFUP_AC')
ax3.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.87,0.86,0.45,0.76,0.74],color='b',marker='o',label="MC")

#ax4=fig.add_subplot(2, 2, 2)
ax4.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.67,0.68,0.61,0.62,0.64],color='r',marker='o',label='WFUP_AC')
ax4.plot([0.2,0.25,0.3,0.35,0.4,0.45],[0.5,0.87,0.86,0.45,0.76,0.74],color='b',marker='o',label="MC")

plt.show()
