# Python3.7
# author- Roshan KOirala
"""
    Plot Earthquake and Injection Time series

"""
#==============================================================================
#                   Modules
#==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#==============================================================================
#                  Load data
#==============================================================================
# Input Files
file_recent = 'texnet_events.csv'
file_all = 'All_catalog.csv'
file_injection = 'Injection.csv'

#==============================================================================
# plot earthquakes
df = pd.read_csv(file_recent)
date_eq_recent  = df['Date'].tolist()
mag_eq_recent = df['Mag'].tolist()


df = pd.read_csv(file_all)
date_eq_all  = df['Date'].tolist()
mag_eq_all = df['Mag'].tolist()

df = pd.read_csv(file_injection)
date_inj = df['Date'].tolist()
inj_10932828  = df['10932828'].tolist()
inj_10933170  = df['10933170'].tolist()
inj_38938320  = df['38938320'].tolist()
inj_38930873  = df['38930873'].tolist()

###============================================================================
fig, ax1 = plt.subplots()


ax1.plot(date_inj, inj_38930873, 'orange',label='API_38930873')
ax1.plot(date_inj, inj_10933170, 'b', label='API_10933170')
ax1.plot(date_inj, inj_38938320, 'c', label='API_38938320')
ax1.plot(date_inj, inj_10932828, 'k', label='API_10932828')

ax2 = ax1.twinx()
ax2.stem(date_eq_recent, mag_eq_recent, 'r', markerfmt='o')

ax1.set_xlabel('Year')
ax2.set_ylabel('Recent Earthquake', color='g')
ax1.set_ylabel('Injection Volume (Barrel)', color='b')
ax1.legend(loc='upper left')

plt.show()


#==============================================================================
dir_out = 'plots'
plot_recent_1 = '4well_injection.png'

plt.savefig('%s/%s'%(dir_out, plot_recent_1))
#==============================================================================

fig, ax1 = plt.subplots()
ax1.stem(date_eq_recent, mag_eq_recent, 'r', markerfmt='o')
ax1.set_xlabel('Year')
ax1.set_ylabel('Earthquake - magnitude')

plt.show()
plot_recent_2 = 'Earthquake_latest.png'

plt.savefig('%s/%s'%(dir_out, plot_recent_2))
#==============================================================================
fig, ax1 = plt.subplots()

#ax1.stem(date_eq_all, mag_eq_all, 'r', markerfmt='o')
plt.hist(date_eq_recent, bins=51, color='orange')
ax1.set_xlabel('Year')
ax1.set_ylabel('Frequency')

plt.show()
plot_all = 'Earthquake_all_hist.png'

plt.savefig('%s/%s'%(dir_out, plot_all))
