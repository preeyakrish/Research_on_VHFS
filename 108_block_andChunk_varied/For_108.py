'''
Created on Sep 17, 2014

@author: vembu
'''
# Plotting by varying blocksize and chunksize
import linecache
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import Calling_Utiltiy_seq as cal
from mpldatacursor import datacursor
from mpl_toolkits.mplot3d import Axes3D

def Merging_Input_and_Output ():
    Merge_Write_file = open ('Merge_write.txt','w+')
    Merge_Read_file = open ('Merge_read.txt','w+')       
    print('inside merging_in_out_func')
    ifile = '108_Block_Chunk.txt'
    totlines = cal.file_total_lines(ifile)
    i = 1
    while (i <= totlines):
        if (i%2 == 0):
            retrieved_Input_line1 = linecache.getline(ifile, i)
            Input1 = retrieved_Input_line1.strip().split(',')
            #print (Input1)
            retrieved_Output_line1 = linecache.getline('Output_file.txt',i)
            output1 = retrieved_Output_line1.strip().split(' ')
            #print (output1)
            a1 = int(Input1[0])/1024
            temp1 = int(Input1[1])/1024
            b1 = int(temp1)/1024
            temp = int(Input1[2])/1024
            c1 = temp/1024
            d1 = (output1[len(output1)-2])
            e1 = output1[len(output1)-1]
            Merge_Read_file.write(str(a1)+"\t"+str(b1)+"\t"+str(c1)+"\t"+str(d1)+"\t"+str(e1))
            Merge_Read_file.write("\n")
            print ("written into Merge_read_file")
        else:
            retrieved_Input_line2 = linecache.getline(ifile, i)
            Input2 = retrieved_Input_line2.strip().split(',')
            retrieved_Output_line2 = linecache.getline('Output_file.txt',i)
            output2 = retrieved_Output_line2.strip().split(' ')
            #print (Input2)
            #print(output2)
            a2 = int(Input2[0])/1024
            temp1 = int(Input2[1])/1024
            b2 = temp1/1024
            temp = int(Input2[2])/1024
            c2 = temp/1024
            print (len(output2))
            d2 = (output2[len(output2)-2])
            e2 = (output2[len(output2)-1])
            Merge_Write_file.write(str(a2)+"\t"+str(b2)+"\t"+str(c2)+"\t"+str(d2)+"\t"+str(e2))
            Merge_Write_file.write("\n")
            print ("written into Merge_write_file")
        i += 1
        
    Merge_Write_file.close()
    Merge_Read_file.close()
         
    
def Graph_write():
    print ('inside Graph_write graph')
    Plot3 = np.loadtxt('Merge_write.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    pl.title('Write :: Chunk_and_Block Size vs Speed')    
    pl.xlabel('Block Size in MB')
    pl.ylabel('Chunk Size in MB')

  
    x = Plot3[:9,1]
    y = Plot3[:9,2]
    z = Plot3[:9,3]
    yerr = Plot3[:9,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='b')
    ax.plot(x,y,zs = z, zdir = z,label = '64MB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)
    
    
    
    x = Plot3[9:18,1]
    y = Plot3[9:18,2]
    z = Plot3[9:18,3]
    yerr = Plot3[9:18,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='g')
    pl.plot(x,y,zs = z, zdir = z,label = '128MB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)
    #pl.show()
    
    x = Plot3[18:27,1]
    y = Plot3[18:27,2]
    z = Plot3[18:27,3]
    yerr = Plot3[18:27,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='m')
    pl.plot(x,y,zs = z, zdir = z,label = '512MB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)
    
    x = Plot3[27:36,1]
    y = Plot3[27:36,2]
    z = Plot3[27:36,3]
    yerr = Plot3[27:36,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='y')
    pl.plot(x,y,zs = z, zdir = z,label = '1GB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)

    x = Plot3[36:45,1]
    y = Plot3[36:45,2]
    z = Plot3[36:45,3]
    yerr = Plot3[36:45,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='c')
    pl.plot(x,y,zs = z, zdir = z,label = '1.5GB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)

    x = Plot3[45:54,1]
    y = Plot3[45:54,2]
    z = Plot3[45:54,3]
    yerr = Plot3[45:54,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='r')
    pl.plot(x,y,zs = z, zdir = z,label = '2GB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)

    pl.show()
    
    pl.savefig('Blk_and_chunk_varied_Write.ps')
    pl.savefig('Blk_and_chunk_varied_Write.png')
    pl.savefig('Blk_and_chunk_varied_Write.pdf')
    print ('endddd')
    
    plt.close(fig)

def Graph_Read():
    print ('inside Graph_Read graph')
    Plot3 = np.loadtxt('Merge_read.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    pl.title('Read :: Chunk_and_Block Size vs Speed')    
    pl.xlabel('Block Size in MB')
    pl.ylabel('Chunk Size in MB')

  
    x = Plot3[:9,1]
    y = Plot3[:9,2]
    z = Plot3[:9,3]
    yerr = Plot3[:9,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='b')
    ax.plot(x,y,zs = z, zdir = z,label = '64MB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)
    
    
    
    x = Plot3[9:18,1]
    y = Plot3[9:18,2]
    z = Plot3[9:18,3]
    yerr = Plot3[9:18,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='g')
    pl.plot(x,y,zs = z, zdir = z,label = '128MB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)
    #pl.show()
    
    x = Plot3[18:27,1]
    y = Plot3[18:27,2]
    z = Plot3[18:27,3]
    yerr = Plot3[18:27,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='m')
    pl.plot(x,y,zs = z, zdir = z,label = '512MB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)
    
    x = Plot3[27:36,1]
    y = Plot3[27:36,2]
    z = Plot3[27:36,3]
    yerr = Plot3[27:36,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='y')
    pl.plot(x,y,zs = z, zdir = z,label = '1GB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)

    x = Plot3[36:45,1]
    y = Plot3[36:45,2]
    z = Plot3[36:45,3]
    yerr = Plot3[36:45,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='c')
    pl.plot(x,y,zs = z, zdir = z,label = '1.5GB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)

    x = Plot3[45:54,1]
    y = Plot3[45:54,2]
    z = Plot3[45:54,3]
    yerr = Plot3[45:54,4]
    #plt.xscale('log')
    #pl.errorbar(x,y,yerr,ecolor='r')
    pl.plot(x,y,zs = z, zdir = z,label = '2GB')
    #pl.legend(loc = 'upper left', numpoints = 1)
    datacursor(display='multiple', draggable=True)

    pl.show()
    
    pl.savefig('Blk_and_chunk_varied_Read.ps')
    pl.savefig('Blk_and_chunk_varied_Read.png')
    pl.savefig('Blk_and_chunk_varied_Read.pdf')
    print ('endddd')
    
    plt.close(fig)

Merging_Input_and_Output()
Graph_write()
Graph_Read()

