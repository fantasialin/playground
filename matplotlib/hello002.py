import matplotlib.pyplot as plt
import numpy as np
import math
import random

plt.axis([0,5,0,20])
plt.title('hello 002 matplotlib!', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.text(1.1, 12, r'$y = x^2$', fontsize=20, bbox={'facecolor':'yellow', 'alpha':0.2})
plt.grid(True) # show grid line
# [1,2,3,4] as X values, [1,4,9,16] as Y values
plt.plot([1,2,3,4], [1,4,9,16], 'bo')
plt.legend(['First series'])
plt.show()


plt.axis([0,5,0,20])
plt.title('hello 002 matplotlib!', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.text(1.1, 12, r'$y = x^2$', fontsize=20, bbox={'facecolor':'yellow', 'alpha':0.2})
plt.grid(True) # show grid line
# [1,2,3,4] as X values, [1,4,9,16] as Y values
plt.plot([1,2,3,4], [1,4,9,16], 'bo')
plt.plot([1,2,3,4], [0.8,3.5,8.2,15.3], 'r*')
plt.plot([1,2,3,4], [0.5,2.3,7.2,11.6], 'g^')
plt.legend(['First series','Second series','Third series'], loc=2)
#save chart into image file
plt.savefig('hello002.png')
plt.show()

# 5,2 inches DPI=100 --> 500,200 pixels
fig, ax = plt.subplots(figsize=(5,2))
for label in ax.get_xaxis().get_ticklabels():
    label.set_fontweight("bold")
plt.show()

import matplotlib
print(f'matplotlib backend --> {matplotlib.get_backend()}')