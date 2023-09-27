import matplotlib.pyplot as plt
import numpy as np
import math
import random
import pandas as pd
import datetime
import matplotlib.dates as mdates

df = pd.DataFrame({ 'year':2015,
                    'month':[1,1,2,2,3,3,4,4],
                    'day':[13,18,3,21,15,24,8,24],
                    'readings': [12,22,25,20,18,15,17,14]})

df['events'] = pd.to_datetime(df[['year', 'month', 'day']])
print(df)

plt.plot(df['events'],df['readings'])
plt.show()

months = mdates.MonthLocator()
days = mdates.DayLocator()
timeFmt = mdates.DateFormatter('%Y-%m')
fig, ax = plt.subplots(figsize=(6,3))
plt.plot(df['events'],df['readings'])
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)
plt.show()