# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:34:12 2018
Search your file of interest here: http://soleil.i4ds.ch/solarradio/callistoQuicklooks/
Save link to the url below
Lecture 2.3/8 How to access data from the e-Callisto website (central archive)

@author: Christian Monstein
"""

import urllib
from astropy.io import fits
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm
 
url = 'http://soleil.i4ds.ch/solarradio/data/2002-20yy_Callisto/2011/08/09/BLEN7M_20110809_080004_25.fit.gz'
 
print ("Downloading FIT-file with urllib from: "+url)
myfile = url.rsplit('/', 1)[1] # extract filename from URL
#urllib.urlretrieve(url, myfile)  # Python 2.7
urllib.request.urlretrieve(url,myfile) # Python 3.7

hdu   = fits.open(myfile)
data  = hdu[0].data.astype(np.float32)
freqs = hdu[1].data['Frequency'][0] # extract frequency axis
time  = hdu[1].data['Time'][0] # extract time axis
hdu.close()

#------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
extent = (time[0], time[-1], freqs[-1], freqs[0])
plt.imshow(data, aspect = 'auto', extent = extent, cmap=cm.CMRmap, vmin=89,vmax=140) 
# cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
# cm.gnuplot, cm.gnuplot2, cm.CMRmap, cm.plasma, cm.magma
plt.tick_params(labelsize=14)
plt.xlabel('Time [s] of FIT-file: ' + myfile,fontsize=15)
plt.ylabel('Plasma frequency [MHz]',fontsize=15)
plt.title('FIT file taken directly from Callisto website in Switzerland.',fontsize=15)
plt.savefig(myfile + ".png")
#------------------------------------------------------------------------------