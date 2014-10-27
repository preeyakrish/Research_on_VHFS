'''
Created on Sep 11, 2014

@author: vembu
'''

import numpy as np
import pylab as pl



def Graph2():
    print ('inside plot2 graph')
    Plot3 = np.loadtxt('Plot1_write.txt')
    pl.xlim(0,2800)
    
    x = Plot3[:,0]
    y = Plot3[:,1]
    yerr = Plot3[:,2]
    pl.errorbar(x,y,yerr, ecolor = 'g',label='nnn')
    pl.legend(loc = 'best', numpoints = 1,bbox_to_anchor = (1.0, 0.5))
    pl.show()
    
Graph2()
    

