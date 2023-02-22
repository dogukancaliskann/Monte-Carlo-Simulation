# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:21:52 2023

@author: dogukan1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from scipy.stats import norm

data2 = pd.read_excel(r'\dataformontecarlo2.xlsx').reset_index(drop=True)

data2['tarih'] = pd.to_datetime(data2['tarih'])  
data2.sort_values(by='tarih', inplace=True)
data2.info()
data2.head()

#Plotting the endorsement values of Arçelik.
plt.figure(figsize=(15,6))
plt.plot_date(data2['tarih'], data2['ciro'], 'g')
plt.xticks(rotation=70)


#Calculating of logaritmic returns. 
log_returns = np.log(1+data2['ciro'].pct_change())
log_returns.head()

#Density of logaritmic returns. As we can clearly see, log returns are normally distributed.
plt.figure(figsize = (15,6))
sns.distplot(log_returns.iloc[1:])

#Plotting log returns
log_returns.plot(figsize = (15,6))


#Parameters that we are going use in Monte Carlo Simulations. 
u = log_returns.mean() #Mean of logaritmic returns
var = log_returns.var() #Variance of logaritmic returns
stdev = log_returns.std() #Standart deviation of logaritmic returns.
drift = u - (0.5*var) # Drift is a constant directional movement. You can search the importance of drift in Monte Carlo.



#Monte Carlo Simulations
quartile = 12 #As I said in ReadME section, I want to simulate the scenario, which will happen after 12 quartiles.
trials = 10000 #10,000 simulations

Z = norm.ppf(np.random.rand(quartile, trials))

daily_returns = np.exp(drift + stdev * Z) #Daily returns



#For Monte Carlo Simulation, we are going to assign the last endorsement(ciro) value to beginning of our simulations.

q_paths = np.zeros_like(daily_returns) #Creating an array with the shape of daily_returns (12,10000)
q_paths[0] = data2['ciro'].iloc[-1] #Assigning the last value to beginning of the simulations.


#We are ready to make simulations begin.
#For loop is going to simulate the endorsement values of Arçelik Company for the next 12 quartiles. 
for t in range(1, quartile):
    q_paths[t] = q_paths[t-1]*daily_returns[t]
    
q_paths.shape


#Fortunately for us, we did not be forced to look which value we reach after 12 quartiles manually.
#Let's plotting the result of 10,000 Monte Carlo Simulations.
plt.figure(figsize=(15,6))
plt.plot(pd.DataFrame(q_paths))

sns.distplot(pd.DataFrame(q_paths).iloc[-1])
plt.xlabel("Price after 12 Quartile")

#This hard to see how many simulations, which reached the real value after 12 quartiles.
#Therefore, we are going to specialize the axis with the range of x-axis, which contains the real value 39,191.88
fig, ax = plt.subplots()
sns.distplot(pd.DataFrame(q_paths).iloc[-1])
ax.set_xlim(38000,39200)
plt.show()

#As we can see from plot, the density of monte carlo simulations, which have reached the our target value after 12 quartiles is too low.






