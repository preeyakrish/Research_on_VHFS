'''
Created on Sep 11, 2014

@author: vembu
'''
from pymongo import Connection
import os
import cmd
import subprocess
import numpy as np
import linecache
#import Conf_XML_Update_seq as conf

def Calling_Utility(Enableread,iteration,ifile1,lno):
    uout_file_name = 'utilityout.txt'
    uout = open(uout_file_name, 'a')
    wordsin = []
    itera = int (iteration)
    count = 0
    for i in range(itera):         
        cmd = './CMDFinal1'
        return_code = subprocess.call(cmd, stdout=uout)
        print(return_code)        
        print("executed driver test for %s" %count)
        os.system('echo 3 > /proc/sys/vm/drop_caches')
        print("echo command")
        if (not (int(Enableread)) and not (i == itera-1)):
            print ("inside if condition of writeclean")
            os.system('rm -rf ./chunkfile/*')
            print ("removed chunkfiles")
            c = Connection('localhost', 27017)
            c.drop_database('makdatabase')   
            print("dropped db")    
        else:
            print ("writeElseeeeeeeeee")
        count = count + 1
    uout.close() 
    if int(Enableread):
        print ("inside if condition of read write")
        os.system('rm -rf ./chunkfile/*')
        print ("removed chunkfiles")
        c = Connection('localhost', 27017)
        c.drop_database('makdatabase')   
        print("dropped db")    
    else:
        print ("Elseeeeeeeeee")
    read_output_file_of_utility(uout_file_name,ifile1,lno)
    print (count) 

def read_output_file_of_utility(uout,ifile1,lno):
    sout_file_name = 'sout.txt' 
    sout = open('sout.txt','w+')
    inf = open(uout,'r')
    alllines = inf.readlines()
    for sline in alllines:
        if sline.startswith('-DBTIME'):
            sout.write(sline)
    sout.close()
    calc_mean_std(sout_file_name,ifile1,lno)
    

def calc_mean_std(sout_file_name,ifile1,lno):
    speed =[]
    time = []
    sout1 = open(sout_file_name,'r')
    alllines = sout1.readlines()
    for sline in alllines:
        wordsin = sline.strip().split(' ')
        speed.append(float(wordsin[len(wordsin)-1]))
        time.append(float(wordsin[len(wordsin)-3]))
     
    meantime = np.mean(time)
    meantime = round(meantime,2)
    meanspeed = np.mean(speed)
    meanspeed = round(meanspeed,2)
    stdspeed = np.std(speed)
    stdspeed = round(stdspeed,2) 
    print (meantime)
    print (meanspeed)
    print (stdspeed)
    sout1.close()
    generating_ouput_file(ifile1,lno,meantime,meanspeed,stdspeed)
    
def generating_ouput_file(ifile1,lno,meantime,meanspeed,stdspeed):
    outf = open('Output_file.txt','a')
    retrieved_Input_line1 = linecache.getline(ifile1, lno)
    Input1 = retrieved_Input_line1.strip().split(',')
    outf.write(Input1[0]+' '+Input1[1]+' '+Input1[2]+' '+str(meantime)+' '+str(meanspeed)+' '+str(stdspeed))
    outf.write('\n')
    outf.close()
    
def file_total_lines (file_name):
    ofile = open(file_name,'r')
    file = ofile.readlines()
    count = 0
    for i in file:
        count +=1
    print (count)
    return count
    




    
    
    
    
    