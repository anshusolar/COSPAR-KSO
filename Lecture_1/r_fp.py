# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:35:36 2017
Lecture 1.2/9 Plot a mathematical function, play with log-scale for x- and y-axis
@author: Christian
"""
from matplotlib import pyplot as plt
import numpy as np

#--------------------------------------------------------------------------------
plt.figure(figsize=(10,7))
r = np.arange(1.0, 10.0, 0.01)  # create a list of radii
fp = 307.86 * r**(-3.64) - 0.14 # equation from Nat Gopalswamy
#plt.plot(r,fp,'-sb') # plot function single dots blue
plt.plot(r,fp,'-g') # plot function line green

plt.plot(1.34,109,'-+r',markersize=20) # single point

plt.xlabel("Solar radius",size=22)
plt.ylabel("Plasma frequency [MHz]",size=22)
plt.title("Plasma frequency vs solar radius", fontsize=22)
plt.grid(True)
#plt.xlim(0,10)
#plt.ylim(0,200)
plt.xscale('log')
plt.yscale('log')
plt.tick_params(labelsize=22)
plt.savefig("plasmafrequency.png")
plt.show()

fp = 307.86 * 2.4**(-3.64) - 0.14
print ('fp= ',fp)

#--------------------------------------------------------------------------------
