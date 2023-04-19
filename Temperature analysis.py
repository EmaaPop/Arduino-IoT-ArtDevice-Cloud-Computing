import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.pyplot import MultipleLocator

data = pd.read_csv("Temperature-Temperature.csv")

xdata = data.loc[:,'time']
ydata = data.loc[:,'value']

x = []
y = []

for i in range(0,len(ydata)):
    temp = float(ydata[i])
    if temp > 0:
        y.append(temp)
#         colors.append(temp)
        
        try:
            time_obj = datetime.strptime(xdata[i], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            time_obj = datetime.strptime(xdata[i], "%Y-%m-%dT%H:%M:%SZ")

        target_time_str = datetime.strftime(time_obj, "%Y/%m/%d %H:%M:%S")
        
        x.append(target_time_str)

print(len(x),len(y))
print(x)

x_num = len(x)
x_interval = x_num // 10 + 1

x_major_locator=MultipleLocator(500)

plt.title(u"Temperature: from 10:17 to 10:43",size=15) 
plt.xlabel(u'time',size=15) 
plt.ylabel(u'temp',size=15) 

plt.scatter(x, y, c=y, cmap=plt.cm.RdBu_r, edgecolor='none', s=40, linewidth=0.0, alpha=1)

plt.gca().xaxis.set_major_locator(x_major_locator)

plt.show() 
