# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:07:53 2024

@author: AneleMahlangu
"""

# for i in range(1,10):
#     print(i)
"""    
import numpy as np
x = np.arange(2,11,0.3)
print(x)
list(x)"""
"""
#numpy arange
import matplotlib.pyplot as plt
import numpy as np
print("just using python:")
for i in np.arange(2,11,0.3):
    print(i)
    """
 ##squaring numbers from 1 to 5
# squares =[]
# for i in np.arange(1,6):
#     squares.append(i**2)
# print(i)
# ##ORRRRR
# squares = np.arange(1,6)**2
# print(squares)
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,6)
y = x**2
plt.plot(x,y, "r")
plt.show

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('noisydata.csv',skiprows=1,delimiter=",")
data_avg = np.mean(data,1)
print(data_avg)
pressure=data[:,0] #all rows first column
flowrate=data[:,1] #all rows second column
fit=np.polyfit(pressure, flowrate, 3) #polynomials
flowfit=np.polyval(fit,pressure)
plt.plot(pressure, flowrate,"go")
plt.plot(pressure, flowfit,"k-")
plt.xlabel("pressure(pa)")
plt.ylabel("mmmm")