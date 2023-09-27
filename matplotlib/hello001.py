import matplotlib.pyplot as plt
import numpy as np
import math
import random

# [1,2,3,4] as Y values, [0,1,2,3] as X values
plt.plot([1,2,3,4])
plt.show()

# [1,2,3,4] as X values, [1,4,9,16] as Y values
plt.plot([1,2,3,4], [1,4,9,16])
plt.show()

# third argument 'ro' to plot red dot.
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.show()

# X axis form 0 - 5, Y axis from 0 - 20
plt.axis([0,5,0,20])
plt.title('Hello matplotlib!')
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.show()

# 0 - 2.5 step 0.05
t = np.arange(0, 2.5, 0.05)
y1 = np.sin(math.pi * t)
y2 = np.sin(math.pi * t + math.pi/2)
y3 = np.sin(math.pi * t - math.pi/2)
plt.plot(t,y1, 'b*', t, y2, 'g^', t, y3, 'ys')
plt.show()

plt.plot(t,y1, 'b--', t, y2, 'g', t, y3, 'y-.')
plt.show()

plt.plot([1,2,4,2,1,0,1,2,1,4], linewidth=2.0)
plt.show()

# add random value
data = random.sample(range(100), k=100)
plt.plot(data, linewidth=2.0)
plt.show()

# figure size = (1000, 300)
f = plt.figure(figsize=(10,3))
ax = f.add_subplot(121) # 121 is for setting the mode of subdivision and determines which is the current subplot.
ax2 = f.add_subplot(122) # 122 is for setting the mode of subdivision and determines which is the current subplot.
x = np.linspace(0,4,1000)
ax.plot(x, np.sin(x))
ax2.plot(x, np.cos(x), 'r:')
plt.show()

f = plt.figure(figsize=(10,3))
ax = f.add_subplot(211) # 211 is for setting the mode of subdivision and determines which is the current subplot.
ax2 = f.add_subplot(212) # 212 is for setting the mode of subdivision and determines which is the current subplot.
x = np.linspace(0,4,1000)
ax.plot(x, np.sin(x))
ax2.plot(x, np.cos(x), 'r:')
plt.show()

t = np.arange(0,5,0.05)
y1 = np.sin(2*np.pi*t)
y2 = np.sin(2*np.pi*t)
plt.subplot(211)
plt.plot(t, y1, 'b-.')
plt.subplot(212)
plt.plot(t, y2, 'r--')
plt.show()


plt.subplot(121)
plt.plot(t, y1, 'b-.')
plt.subplot(122)
plt.plot(t, y2, 'r--')
plt.show()