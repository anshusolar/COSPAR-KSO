# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 19:19:13 2016
This script sends png-images from a source drive to a webserver
once the file is copied, it is deleted from the sourc-path
Lecture 9.1/9
@author: Christian
"""

import ftplib
import os
import glob

sourceFilePath = "C:/MyPython/Lecture_9/FTP/" # Edit !!!
destinationFilePath = "PNG/" # Edit !!!
server   = "internetaddressofmywebserver" # Edit !!!
username = "myusername" # Edit !!!
password = "mypassword"  # Edit !!!

ftp = ftplib.FTP(server)
ftp.login(username, password)
ftp.set_pasv(True)
ftp.cwd(destinationFilePath)
os.chdir(sourceFilePath)

myfilter = sourceFilePath + "*.png"
liste = glob.glob(myfilter)

liste.sort()
i = 0
for ff in liste:
    print (ff)
    head,filename = os.path.split(ff)
    myfile = open(ff, 'rb')
    ftp.storbinary('STOR ' + filename, myfile)
    i = i +1
    myfile.close()
    os.remove(filename)
    
ftp.close()

print (i,"files transferred to my FTP account on the central webserver.")

