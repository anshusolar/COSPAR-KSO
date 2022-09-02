# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 17:33:00 2018
Lecture 4.5/9 Download event-list from SWPC/NOAA FTP-server
@author: Hitsch
"""
import urllib
 
#-----------------------------------------------------------------
url = 'ftp://ftp.swpc.noaa.gov/pub/warehouse/2019/'
myfile = '2019_events.tar.gz' # Edit !!!
myurl = url + myfile
print ("Downloading Event-file with urllib from: " + myurl)
#urllib.urlcleanup() # Python 2.7
#urllib.urlretrieve(url, myfile)  # Python 2.7
urllib.request.urlretrieve(url,myfile)


print("Do not forget to unip and untar the file!")
print ("Find a solution in python.")
#-----------------------------------------------------------------
