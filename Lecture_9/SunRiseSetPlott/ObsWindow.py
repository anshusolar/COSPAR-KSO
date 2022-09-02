# -*- coding: utf-8 -*-
"""
This script tracks the Sun in parallactic mode (local hour angle and declination)
Carefully check paramter in MyLocation
It is sufficient to execute this script once every 4...5 minutes
Created on Thu Sep 14 20:13:50 2017
Lecture 9.4/9
@author: Monstein
"""
# http://rhodesmill.org/pyephem/tutorial.html
# http://rhodesmill.org/pyephem/quick#other-observer-methods
#------------------------------------------------------------------------------

import ephem # python 2.7
#import astropy.ephem as ephem # python 3.?
from matplotlib import pyplot as plt
import numpy as np

#defining position Arecibo: 8°29'14.6"N 66°52'17.9"W
location  = 'Arecibo, Puerto Rico'
longitude = '-66.8'
latitude  = '8.5'

plt.figure(figsize=[10,6])
#plt.step(t,azi,'-',color='red') #o,+,
plt.xlabel("Time of the day [UT]",fontsize=15)
plt.ylabel("Month of the year ",fontsize=15)
plt.title("Observation Coverage " + location,fontsize=15)
plt.xlim(0,24)# UT
plt.ylim(1,12) # MHz
plt.grid()
plt.tick_params(labelsize=10)
plt.xticks(np.arange(0, 24+1, 1.0))
my_yticks = [' ','JAN  ','FEB  ','MAR  ','APR  ','MAY  ','JUN  ','JUL  ','AUG  ','SEP  ','OCT  ','NOV  ','DEC  ']
plt.yticks(np.arange(0, 12+1, 1.0), my_yticks,rotation=90)
#plt.yticks(np.arange(1, 12+1, 1.0))


#defining an observer
obs = ephem.Observer()

obs.long = ephem.degrees(longitude)
obs.lat = ephem.degrees(latitude)


#defining date
date = '2020/01/08 12:00:00'

for month in range(1,13):
    for day in range(1,31):
        date = '{:4d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d}'.format(
           2020,month,day,12,0,0)
                
        obs.date = ephem.Date(date)
        
        sun = ephem.Sun(obs)
        
        r1 = obs.next_rising(sun)
        s1 = obs.next_setting(sun)
        n1 = obs.next_transit(sun)
                
        t1 = r1.datetime().hour + r1.datetime().minute/60. + r1.datetime().second/3600
        #print t1
        t2 = s1.datetime().hour + s1.datetime().minute/60. + s1.datetime().second/3600
        #print t2
        t3 = n1.datetime().hour + n1.datetime().minute/60. + n1.datetime().second/3600
        #print t2
        y = month+day/30. -1.0
        plt.plot(t1,y,'*g')
        plt.plot(t2,y,'*b')
        plt.plot(t3,y,'+r')

        
plt.plot(t1,y,'*g',label='Sun rise')
plt.plot(t2,y,'*b',label='Sun set')
plt.plot(t3,y,'+r',label='Sun transit')
plt.legend(loc='upper left')
plt.show()
plt.savefig(location+'.png')