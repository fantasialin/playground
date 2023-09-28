import matplotlib.pyplot as plt
import numpy as np

#line charts
x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(3*x)/x
plt.plot(x,y)
plt.show()


y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()


plt.plot(x, y, 'k--', linewidth=3)
plt.plot(x, y2, 'm-.')
plt.plot(x, y3, color='#87a3cc', linestyle='--')
plt.legend(['1st', '2nd', '3rd'])
plt.show()

plt.plot(x, y, color='b')
plt.plot(x, y2, color='r')
plt.plot(x, y3, color='g')
plt.legend(['1st', '2nd', '3rd'])
plt.xticks([-2*np.pi,-np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$',r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-1,0,1,2,3],
           [r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
plt.show()

plt.plot(x, y, color='b')
plt.plot(x, y2, color='r')
plt.plot(x, y3, color='g')
plt.xticks([-2*np.pi,-np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$',r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-1,0,1,2,3],
           [r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()

plt.plot(x, y, color='b')
plt.plot(x, y2, color='r')
plt.plot(x, y3, color='g')
plt.xticks([-2*np.pi,-np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$',r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-1,0,1,2,3],
           [r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}=1$',
             xy=[0,1], xycoords='data',
             xytext=[30,30],
             fontsize=16,
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->",
             connectionstyle="arc3, rad=.2"))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()