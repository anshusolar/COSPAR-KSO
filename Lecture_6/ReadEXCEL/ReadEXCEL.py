# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:55:41 2018
Lecture 6.3/9 read an EXCEL file
@author: C. Monstein
"""

import pandas
import matplotlib.pyplot as plt 
import numpy as np

excel = pandas.read_excel('Callisto_DataStatus_V44e.xlsx',header=4,skipfooter=5)

print ('These are the columns:\n ',excel.columns)

country = excel['Country'].values #get the values for a given column
print ("\n\nHere is the column with the Country':\n",country)
N = len(country)

frange = excel['Antenna'].values #get the values for a given column
print ("\n\nHere is the column with the title 'Frequency range':\n",frange)

delivered = excel['delivered'].values #get the values for a given column

plt.figure(figsize=(15,6))
x = country
plt.bar(x,delivered)
plt.xticks(rotation=90)
plt.xlabel('Country hosting one or more Callisto',size=16)
plt.ylabel('Units',size=16)
st = 'Total instruments: {:4.0f}'.format(np.sum(delivered))
plt.text(0,10.4,st,size=15,color='b')
plt.title('Callisto delivered per country, in total {:3.0f} countries.'.format(N),size=18)
plt.grid('true',color='g')
plt.tick_params(labelsize=14)
plt.tight_layout()
plt.show()
plt.savefig('callisto.png')
