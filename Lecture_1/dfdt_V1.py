# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:35:36 2017
Lecture 1.3/9 Plot a mathematical function and save in different graphics format
@author: Christian
"""
from matplotlib import pyplot as plt
import numpy as np

#--------------------------------------------------------------------------------

plt.figure(figsize=(10,7))
fp = np.arange(10, 210, 10)
dfdt  = 4.1e-4 * fp**1.275
dfdt1 = 4.2e-4 * fp**1.3
plt.plot(fp,dfdt,'-sb')  # squares connected by a line in blue
plt.plot(fp,dfdt1,'-or')  # squares connected by a line in blue
plt.xlabel("Plasma frequency [MHz]",size=18)
plt.ylabel("df/dt [MHz/s]",size=18)
plt.title("Type II statistical drift rate", size=18)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.tick_params(labelsize=20)
plt.plot(200,0.334478,'Xr')  # measured driftrate MHz/s blue square
plt.plot(33.35,0.08,'Xr')  # measured driftrate MHz/s blue square
plt.plot(31.9,0.065,'og')  # measured driftrate MHz/s green circle
plt.plot(24.9,0.071,'dm')  # measured driftrate MHz/s magenta diamond
plt.plot(154.9,0.081,'+m')  # measured driftrate MHz/s magenta diamond

plt.xticks(np.arange(13,210, 26.0))
   
plt.savefig("Driftrate.png")
plt.savefig("Driftrate.pdf")
plt.savefig("Driftrate.eps")
plt.savefig("Driftrate.tif")

plt.savefig("test.eps", 
       bbox_inches='tight', 
       transparent=True,
       pad_inches=0)
#--------------------------------------------------------------------------------
