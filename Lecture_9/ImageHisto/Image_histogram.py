# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:33:38 2018
Lecture 9.2/9 Plot histogram of an image

@author: Chr. Monstein
"""

import matplotlib.pyplot as plt
from pylab import imread

#-----------------------------------------------------------------------------

imgfile = '20180527_120003.jpg'

image = imread(imgfile) 
plt.figure(figsize=(5,7))
plt.imshow(image)
plt.xlabel('x-axis pixel')
plt.ylabel('y-axis pixel')
plt.title('Two Ethiopian girls')

plt.figure(figsize=(8,6))
plt.hist(image.ravel(), bins=256, range=(0.0, 256.0), color='g')
plt.xlabel('Bins ',fontsize=12)
plt.ylabel('Counts',fontsize=12)
plt.title('Brightnes-Histogram of 2 Ethiopian girls',fontsize=12)
plt.tick_params(labelsize=10)
plt.show()
#-----------------------------------------------------------------------------
