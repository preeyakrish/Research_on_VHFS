'''
Created on 16-Oct-2014

@author: root
'''
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from mpldatacursor import datacursor

def Graph_Instant_boot():
    print ('inside Graph_Instant_boot graph')
    Plot1 = np.loadtxt('Output_VHFS_Instant_boot.txt')
    Plot2 = np.loadtxt('Output_VHFS_Instant_boot_2.txt')
    Plot3 = np.loadtxt('VHD_Output_Boot_time_first.txt')
    Plot4 = np.loadtxt('VHD_Output_Boot_time_Second.txt')
    fig = plt.figure()
    pl.subplot(311)
    
    pl.title('Instant_Boot_First_time: VHFS vs VHD')    
    pl.xlabel('Incrementals')
    pl.ylabel('Time Taken in secs')
    pl.xlim(-1,11)
    
    x = Plot1[:,0]
    y = Plot1[:,1]
    y2 = Plot3[:,1]
    #yerr = Plot1[:,4]
    #xticks = Plot1[:,1]
    #plt.xticks(xticks)
    #plt.xscale('log')
    #plt.yscale('log')
    #plt.xticks(xticks)
    #pl.errorbar(x,y,yerr,ecolor='b')
    pl.plot(x,y, 'b', label = 'VHFS', marker = 'o')
    pl.plot(x,y2, 'y', label = 'VHD', marker = 'o')
    pl.legend(loc = 'upper right', numpoints = 1)
    datacursor(display='multiple', draggable=True)
    
    pl.subplot(313)
    
    pl.title('Instant_Boot_Second_time: VHFS vs VHD')    
    pl.xlabel('Incrementals')
    pl.ylabel('Time Taken in secs')
    pl.xlim(-1,11)
    
    x = Plot2[:,0]
    y = Plot2[:,1]
    y2 = Plot4[:,1]
    #yerr = Plot1[:,4]
    #xticks = Plot1[:,1]
    #plt.xticks(xticks)
    #plt.xscale('log')
    #plt.yscale('log')
    #plt.xticks(xticks)
    #pl.errorbar(x,y,yerr,ecolor='b')
    pl.plot(x,y, 'b', label = 'VHFS', marker = 'o')
    pl.plot(x,y2, 'y', label = 'VHD', marker = 'o')
    pl.legend(loc = 'upper right', numpoints = 1)
    datacursor(display='multiple', draggable=True)
    #pl.show()
 
    pl.savefig('Instant_boot_VHFS_vs_VHD.ps')
    pl.savefig('Instant_boot_VHFS_vs_VHD.png')
    pl.savefig('Instant_boot_VHFS_vs_VHD.pdf')
    print ('endddd')
    
    plt.close(fig)

Graph_Instant_boot()