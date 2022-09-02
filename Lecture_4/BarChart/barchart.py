# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:39:56 2018
Lecture 4.2/9 Plot bar-chart
@author: Christian Monstein
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------
 
objects = ('Python', 'C++', 'MatLab','Java', 'Perl', 'R', 'IDL', 'Fortran77')
x_pos = np.arange(len(objects))
performance = [10,8,6,5,4,2,1,-1]
 
plt.bar(x_pos, performance, align='center', alpha=0.9,color='r')
plt.xticks(x_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.savefig("MyBarChart.png") 
plt.show()
#-----------------------------------------------------------------------------
