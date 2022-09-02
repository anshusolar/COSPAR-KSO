# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:35:36 2017
Lecture 9.3/9 Plot a mathematical function, save with known dpi
@author: Christian
"""
from matplotlib import pyplot as plt
import numpy as np

#--------------------------------------------------------------------------------
plt.figure(figsize=(10,7))
r = np.arange(1.0, 10.0, 0.01)  # create a list of radii
fp = 307.86 * r**(-3.64) - 0.14 # equation from Nat Gopalswamy
plt.plot(r,fp,'-r',linewidth=7.0) # plot function line green

plt.xlabel("Solar radius",size=22)
plt.ylabel("Plasma frequency [MHz]",size=22)
plt.title("Plasma frequency vs solar radius", fontsize=22)
plt.grid(True)
plt.xlim(0,10)
plt.ylim(0,200)
plt.tick_params(labelsize=22)

plt.savefig("plasmafrequency1.png")
plt.savefig("plasmafrequency2.png",dpi=500)

plt.show()

#--------------------------------------------------------------------------------
