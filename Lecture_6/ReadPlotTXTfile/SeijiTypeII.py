# -*- coding: utf-8 -*-
"""
Created on Thursday, 24.05.2018 during COSPAR workshop
Lecture 6.1/9 
Generates plot of a 'Seiji' text file with several mixed columns (Text and floating point numbers)
Further analysis and plots need to be added....

@author: Chr. Monstein

"""
#--------------------------------------------------------------------------------

from matplotlib import pyplot as plt
import numpy as np
import os
#from Tkinter import Tk # Python 2.7
from tkinter import Tk
#from tkFileDialog import askopenfilename
from tkinter import filedialog

#--------------------------------------------------------------------------------

Tk().withdraw() # 

#myfile = askopenfilename(title = 'Select a *.txt-file containing Time-/Frequency coordinates of type II burst') # show an "Open" dialog box and returns path&file # Python2.7
myfile = filedialog.askopenfilename(title = 'Select a *.txt-file containing Time-/Frequency coordinates of type II burst') # show an "Open" dialog box and return file

#myfile = 'ft2.txt' # for testing only to avoid too many clicks...
fnam = os.path.basename(myfile) # extract filename only in case it contains also the path

"""
#Date      Time       Freq(MHz)  Xpix  Ypix
2010-06-13T05:37:14    298.1746   203   291
2010-06-13T05:38:20    222.2898   244   266
etc.
"""

MyTime    = [] # reserve a list for time
Frequency = [] # reserve a list for column Frequency

f = open(myfile)
i = 0  # counts the lines in the file   

for row in f:
    i = i + 1
    if (i > 1):  # skip header data, e.g. title
        Rows = repr(row) # force any input to become a printable string 
        Rows = Rows.strip()  # get rid of '\n' and similar control characters
        Row  = Rows.split() # split string into separate elements -> kind of vector or list
        dt = Row[0] # Date-/Time-string is the first element of the list 'Line'
        yy = dt[ 1: 5] # extract year
        MM = dt[ 6: 8] # extract month
        dd = dt[ 9:11] # extract day
        hh = dt[12:14] # get hours
        mm = dt[15:17] # get minutes
        ss = dt[18:20] # get seconds
        tx = float(hh) + float(mm)/60.0 + float(ss)/3600.0 # create decimal hour
        MyTime.append(tx) # fill up the list
        
        f0 = Row[1] # gte frequency out of the table
        Frequency.append(float(f0)) # Fill a list with frequency

f.close()

#--------------------------------------------------------------------------------

plt.figure(figsize=(10,7))
tmin = np.min(MyTime)
tx = (MyTime - tmin)*3600.0 # convert absolute into relative time
plt.plot(tx,Frequency,'-X',color='red') #o,+,
plt.title(fnam,fontsize=16)
plt.xlabel("Relative burst time [sec]",size=18)
plt.ylabel("Plasma frequency [MHz]]",size=18)
plt.title("Type II burst of: " + yy + '-' + MM + '-' + dd, size=18)
plt.grid(True) # an option
plt.tick_params(labelsize=20)
#plt.yscale('log') # this is an option to checkout
plt.show()

plt.savefig('TypeII_' + fnam + '.png')
plt.savefig('TypeII_' + fnam + '.pdf')
plt.savefig('TypeII_' + fnam + '.eps')
# other formats may be edded
#--------------------------------------------------------------------------------
# Here you analysis + plotting may start ..
#--------------------------------------------------------------------------------
