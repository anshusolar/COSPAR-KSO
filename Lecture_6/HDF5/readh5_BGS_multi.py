# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 17:12:00 2018
Lecture 6.4/9 read a HDF5 file and plot many spectra
@author: C. Monstein
"""

import h5py
from matplotlib import pyplot as plt
import numpy as np

file_name = 'HIMap_RSG7M_A1_24_MP_PXX_Z0_C0-M9703A_DPUA_20180307_121402.h5'
data = h5py.File(file_name, 'r')
list_of_names = []
data.visit(list_of_names.append)
print (list_of_names)
#
IF = data['FREQUENCY'].value
i0 = data['/P/Phase1'].value
dB = 10.0*np.log10(i0)#[:,40])
RF = IF + 960.0 # local oscillator = 960 MHz
plt.figure(figsize=[18,8])#
plt.plot(RF,dB)
plt.xlabel("Frequency [MHz]",size=17)
plt.ylabel("Relative intensity [dB]",size=17)
plt.title('Spectrum sequence over 146 x 6 s, Bleien Galactic Survey 2018-03-07 at 12:14:02, Switzerland',size=18)
plt.text(1030-2, 135, 'ADS-B interrogation',color="blue",size=15,rotation=90)
plt.text(1090-2, 146, 'ADS-B replay',color="blue",size=15,rotation=90)
plt.text(1176.45-3, 138, 'GPS-L5',color="blue",size=15,rotation=90)
plt.text(1227.7-3, 142, 'GPS-L2',color="blue",size=15,rotation=90)
plt.text(1243.5-3, 140, 'GLONAS-L2',color="blue",size=15,rotation=90)
plt.text(1250-3, 140, 'Radio amateurs',color="blue",size=15,rotation=90)
plt.tick_params(labelsize=14)

plt.ylim([110,160])
plt.xlim([980,1300])
plt.grid(axis='both')
plt.savefig('MultiSpectrum.png')
#
