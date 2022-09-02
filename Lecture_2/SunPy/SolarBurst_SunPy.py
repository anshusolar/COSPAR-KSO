"""
Created on Sat Mar 31 14:34:12 2018
Another library for plotting (SunPy)
Do not forget to install in command window as: pip install sunpy
Lecture 2.10/9 Pseudo calibration

---> https://docs.sunpy.org/projects/radiospectra/en/latest/guide.html#spectrograms <---
@author: Christian Monstein
For Python 3.7-> type in Anaconda prompt: pip install radiospectra
"""

#from sunpy.spectra.sources.callisto import CallistoSpectrogram # Python 2.7

from radiospectra.sources.callisto import CallistoSpectrogram
import matplotlib.pyplot as plt

files = 'KASI_20151104_031505_59.fit.gz'

image = CallistoSpectrogram.read(files)

plt.figure(figsize=(12,8))

image.plot()
plt.xlim((2000,3600)) # express limits in column number 0...3599
plt.savefig(files+'_raw.png')
plt.show()

plt.figure(figsize=(12,8))

img_nobg = image.subtract_bg()
#img_nobg.plot(vmin=-10,vmax=20,colorbar=False)
img_nobg.plot(vmin=-3,cmap='plasma')
plt.xlim((1500,3600)) # express limits in column number 0...3599
plt.savefig(files+'_nobg.png')
plt.show()

#--------------------------------------------------------------------
