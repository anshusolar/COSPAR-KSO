# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:34:12 2018
Search your file of interest here: http://soleil.i4ds.ch/solarradio/callistoQuicklooks/
Save file in the local folder of the Python script
Lecture 2.2/8 How to access data from another folder

@author: Christian Monstein
"""


from astropy.io import fits
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm
 
mypath = 'C:/MyPython/Lecture_2/data/'  # Edit!!!
myfile = 'ALMATY_20110809_080000_59.fit.gz'

hdu   = fits.open(mypath + myfile)
data  = hdu[0].data.astype(np.float32)
freqs = hdu[1].data['Frequency'][0] # extract frequency axis
time  = hdu[1].data['Time'][0] # extract time axis
hdu.close()

#------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
extent = (time[0], time[-1], freqs[-1], freqs[0])
plt.imshow(data, aspect = 'auto', extent = extent, cmap=cm.CMRmap, vmin=100,vmax=140) 
# cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
# cm.gnuplot, cm.gnuplot2, cm.CMRmap, cm.plasma, cm.magma
plt.tick_params(labelsize=14)
plt.xlabel('Time [s] of FIT-file: ' + myfile,fontsize=15)
plt.ylabel('Plasma frequency [MHz]',fontsize=15)
plt.title('FIT file previously saved in another folder.',fontsize=15)
plt.savefig(myfile + ".png")
#------------------------------------------------------------------------------