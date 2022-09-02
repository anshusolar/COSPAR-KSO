# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 12:02:42 2016

Lecture 2.0/9 The most basic Python script to plot a FIT-file from Callisto

@author: cmonstei
"""

import astropy.io.fits as fits
import matplotlib.pyplot as plt 


fds = fits.open('ALMATY_20110809_080000_59.fit.gz')
data = fds[0].data
fds.close()

plt.imshow(fds[0].data, aspect = 'auto')
plt.savefig('mostbasic.png')
plt.show()