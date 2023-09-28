import matplotlib.pyplot as plt
import numpy as np
import math
import random
import pandas as pd
import datetime
import matplotlib.dates as mdates

data = {'series1':[1,3,4,3,5],
        'series2':[2,4,5,2,4],
        'series3':[3,2,3,1,3]}
df = pd.DataFrame(data)
x = np.arange(5)
plt.axis([-1,5,0,7])
plt.plot(x,df)
plt.legend(data, loc=2)
plt.show()

pop = np.random.randint(0,100,100)
n,bins,patches = plt.hist(pop,bins=20)
plt.show()

index = [0,1,2,3,4]
values = [5,7,3,4,6]
plt.bar(index,values)
plt.show()

index = np.arange(5)
values1 = [5,7,3,4,6]
plt.bar(index,values1)
plt.xticks(index,['A','B','C','D','E'])
plt.show()