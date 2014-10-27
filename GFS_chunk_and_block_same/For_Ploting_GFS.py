'''
Created on Sep 17, 2014

@author: vembu
'''
#GFS Plotting where blocksize and chunksize are of equal size ranging from(512k to 512 MB)
import linecache
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import Calling_Utiltiy_seq as cal
from mpldatacursor import datacursor

Merge_Write_file = open ('Merge_write.txt','w+')
Merge_Read_file = open ('Merge_read.txt','w+')

def Merging_Input_and_Output ():
           
    print('inside merging_in_out_func')
    ifile = 'GFS_BK_and_CHUNK_same.txt'
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
         
    
def Graph_GFS_write():
    print ('inside Graph_GFS graph')
    Plot3 = np.loadtxt('Merge_write.txt')
    Plot4 = np.loadtxt('Merge_read.txt')
    fig = plt.figure()
    pl.subplot(311)
    
    pl.title('Write :: Chunk_and_Block Size vs Speed')    
    pl.xlabel('Chunk_and_Block Size in MB')
    pl.ylabel('Speed in MBps')
    #pl.xlim(0,10)
    
    x = Plot3[:,1]
    y = Plot3[:,3]
    yerr = Plot3[:,4]
    xticks = Plot3[:,1]
    #plt.xticks(xticks)
    plt.xscale('log')
    #plt.yscale('log')
    #plt.xticks(xticks)
    pl.errorbar(x,y,yerr,ecolor='b')
    #pl.plot(x,y, 'b-', marker ='o',)
    datacursor(display='multiple', draggable=True)
    #cursor = Dcursor.FollowDotCursor(ax, x, y)
    #plt.show()
    #pl.show()

    
    pl.subplot(313)    
    pl.title('Read :: Chunk_and_Block Size vs Speed')    
    pl.xlabel('Chunk_and_Block Size in MB')
    pl.ylabel('Speed in MBps')
    #pl.xlim(0,10)
    
    x = Plot4[:,1]
    y = Plot4[:,3]
    yerr = Plot4[:,4]
    xticks = Plot4[:,1]
    pl.xticks(xticks)
    plt.xscale('log')
    pl.errorbar(x,y,yerr,ecolor='b')
    datacursor(display='multiple', draggable=True)
    #pl.plot(x,y, 'b-', marker = 'o')
    #pl.show()
    #Dcursor2.DataCursor([write,read])
    pl.show()
    pl.savefig('GFS_Reading.ps')
    pl.savefig('GFS_Reading.png')
    pl.savefig('GFS_Reading.pdf')
    print ('endddd')
    
    plt.close(fig)

Merging_Input_and_Output()
Graph_GFS_write()

