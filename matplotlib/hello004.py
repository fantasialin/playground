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


y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x, y, 'k--', linewidth=3)
plt.plot(x, y2, 'm-.')
plt.plot(x, y3, color='#87a3cc', linestyle='--')
plt.legend(['1st', '2nd', '3rd'])
plt.show()