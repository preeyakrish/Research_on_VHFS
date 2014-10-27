'''
Created on Sep 6, 2014

@author: vembu
'''
import linecache
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

Merge_Write_file = open ('Merge_write.txt','w+')
Plot1_Write_file = open('Plot1_write.txt','w+')
Plot2_Write_file = open ('Plot2_write.txt','w+')
Plot3_Write_file = open ('Plot3_write.txt','w+')
Merge_Read_file = open ('Merge_read.txt','w+')
Plot1_Read_file = open('Plot1_read.txt','w+')
Plot2_Read_file = open ('Plot2_read.txt','w+')
Plot3_Read_file = open ('Plot3_read.txt','w+')

def Merging_Input_and_Output ():
           
    print('inside merging_in_out_func')
    for i in range(1,41):
        if (i%2 == 0):
            retrieved_Input_line1 = linecache.getline('Input_for_Read_Write.txt', i)
            Input1 = retrieved_Input_line1.strip().split(',')
            retrieved_Output_line1 = linecache.getline('output.txt',i)
            output1 = retrieved_Output_line1.strip().split('\t')
            a1 = int(Input1[0])/1024
            b1 = int(Input1[1])/1024
            temp = int(Input1[2])/1024
            c1 = temp/1024
            d1 = (output1[len(output1)-1])
            Merge_Read_file.write(str(a1)+","+str(b1)+","+str(c1)+","+str(d1))
            Merge_Read_file.write("\n")
            print ("written into Merge_read_file")
        else:
            retrieved_Input_line2 = linecache.getline('Input_for_Read_Write.txt', i)
            Input2 = retrieved_Input_line2.strip().split(',')
            retrieved_Output_line2 = linecache.getline('output.txt',i)
            output2 = retrieved_Output_line2.strip().split('\t')
            a2 = int(Input2[0])/1024
            b2 = int(Input2[1])/1024
            temp = int(Input2[2])/1024
            c2 = temp/1024
            print (len(output2))
            d2 = (output2[len(output2)-1])
            Merge_Write_file.write(str(a2)+","+str(b2)+","+str(c2)+","+str(d2))
            Merge_Write_file.write("\n")
            print ("written into Merge_write_file")
        
    Merge_Write_file.close()
    Merge_Read_file.close()
    
def Graph_Input ():
    print('inside graph_in fun')
    for i in range(1,21):
        Plot_Input_line1 = linecache.getline('Merge_write.txt', i)
        Plot_Input1=Plot_Input_line1.strip().split(",")
        Plot_Input_line2 = linecache.getline('Merge_read.txt', i)
        Plot_Input2=Plot_Input_line2.strip().split(",")

        if((i >=1)and(i <=9)):
            Plot1_Write_file.write(Plot_Input1[1]+" "+Plot_Input1[3])
            Plot1_Write_file.write('\n')
            Plot1_Read_file.write(Plot_Input2[1]+" "+Plot_Input2[3])
            Plot1_Read_file.write('\n')
            print ('written plot1')
        elif(i>=10 and i<=14):
            Plot2_Write_file.write(Plot_Input1[2]+" "+Plot_Input1[3])
            Plot2_Write_file.write('\n')
            Plot2_Read_file.write(Plot_Input2[2]+" "+Plot_Input2[3])
            Plot2_Read_file.write('\n')
            print ('written plot2')
        else:
            Plot3_Write_file.write(Plot_Input1[0]+" "+Plot_Input1[3])
            Plot3_Write_file.write('\n')
            Plot3_Read_file.write(Plot_Input2[0]+" "+Plot_Input2[3])
            Plot3_Read_file.write('\n')
            print ('written plot3')

    Plot1_Write_file.close()
    Plot2_Write_file.close()
    Plot3_Write_file.close()
    Plot1_Read_file.close()
    Plot2_Read_file.close()
    Plot3_Read_file.close()

def Graph1():
    print ('inside plot1 graph')
    Plot1 = np.loadtxt('Plot1_write.txt')
    Plot2 = np.loadtxt('Plot1_read.txt')
    fig = plt.figure()
    pl.subplot(311)
    pl.title('Write :: Block Size vs Speed')
    pl.xlabel('Block Size in KB')
    pl.ylabel('Speed in MBps')
    pl.xlim(0,2800)
    
    x = Plot1[:4,0]
    y1 = Plot1[:4,1]    
    pl.plot(x,y1, '--',label='128MB')
    x = Plot1[5:9,0]
    y2 = Plot1[5:9,1]
    pl.plot(x,y2, 'g', label = '2GB')
    pl.legend(loc = 'upper right', numpoints = 1,bbox_to_anchor = (1.0, 0.5))
    
    pl.subplot(313)
    pl.title('Read :: Block Size vs Speed')
    pl.xlabel('Block Size in KB')
    pl.ylabel('Speed in MBps')
    pl.xlim(0,2800)
    
    x = Plot2[:4,0]
    y1 = Plot2[:4,1]    
    pl.plot(x,y1, '--',label='128MB')
    x = Plot2[5:9,0]
    y2 = Plot2[5:9,1]
    pl.plot(x,y2, 'r',label='2GB')
    pl.legend(loc = 'upper right', numpoints = 1,bbox_to_anchor = (1.0, 0.5))  
    
    pl.savefig('Block_Size_VS_Speed.ps') 
    pl.savefig('Block_Size_VS_Speed.png') 
    
    plt.close(fig)
    
    
    
def Graph2():
    print ('inside plot2 graph')
    Plot3 = np.loadtxt('Plot2_write.txt')
    Plot4 = np.loadtxt('Plot2_read.txt')
    fig = plt.figure()
    pl.subplot(311)
    
    pl.title('Write :: Chunk Size vs Speed')    
    pl.xlabel('Chunk Size in MB')
    pl.ylabel('Speed in MBps')
    pl.xlim(0,2800)
    
    x = Plot3[:,0]
    y = Plot3[:,1]
    pl.plot(x,y, 'm',label='512K BlockSize')
    pl.legend(loc = 'best', numpoints = 1,bbox_to_anchor = (1.0, 0.5))
    
    
    pl.subplot(313)    
    pl.title('Read :: Chunk Size vs Speed')    
    pl.xlabel('Chunk Size in MB')
    pl.ylabel('Speed in MBps')
    pl.xlim(0,2800)
    
    x = Plot4[:,0]
    y = Plot4[:,1]
    pl.plot(x,y, 'm',label='512K BlockSize')
    pl.legend(loc = 'best', numpoints = 1,bbox_to_anchor = (1.0, 0.5))
    
    pl.savefig('Chunk_Size_VS_Speed.ps')
    pl.savefig('Chunk_Size_VS_Speed.png')
    
    plt.close(fig)
   
    
def Graph3():
    print ('inside plot3 graph')
    Plot5 = np.loadtxt('Plot3_write.txt')
    Plot6 = np.loadtxt('Plot3_read.txt')
    fig = plt.figure()
    pl.subplot(311)
    pl.title('Write :: Whole Data vs Speed')
    pl.xlabel('Whole Size in GB')
    pl.ylabel('Speed in MBps')
    pl.xlim(0,150)
    
    x = Plot5[:3,0]
    y1 = Plot5[:3,1]    
    pl.plot(x,y1, '--',label='128MB')
    x = Plot5[3:6,0]
    y2 = Plot5[3:6,1]
    pl.plot(x,y2, 'y', label = '2GB')
    pl.legend(loc = 'upper right', numpoints = 1)
    
    pl.subplot(313)
    pl.title('Read :: Whole Data vs Speed')
    pl.xlabel('Whole Size in GB')
    pl.ylabel('Speed in MBps')
    pl.xlim(0,150)
    
    x = Plot6[:3,0]
    y1 = Plot6[:3,1]    
    pl.plot(x,y1, 'y',label='128MB')
    x = Plot6[3:6,0]
    y2 = Plot6[3:6,1]
    pl.plot(x,y2, 'r',label='2GB')
    pl.legend(loc = 'upper right', numpoints = 1)    
    pl.savefig('Whole_Data_VS_Speed.ps')
    pl.savefig('Whole_Data_VS_Speed.png')
    plt.close(fig)
    
def main():
    Merging_Input_and_Output()
    Graph_Input()
    Graph1()
    Graph2()
    Graph3()
main()


