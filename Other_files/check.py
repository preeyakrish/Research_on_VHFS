'''
Created on Sep 11, 2014

@author: vembu
'''


import numpy as np
import linecache


def read_output_file_of_utility():
    sout = open('sout.txt','w+')
    inf = open('outputrand.txt','r')
    alllines = inf.readlines()
    for sline in alllines:
        if sline.startswith('-DBTIME'):
            sout.write(sline)
    sout.close()
    inf.close()
    calc_mean_std()

def calc_mean_std():
    speed =[]
    time = []
    sout1 = open('sout.txt','r')
    alllines = sout1.readlines()
    for sline in alllines:
        wordsin = sline.strip().split(' ')
        speed.append(float(wordsin[len(wordsin)-1]))
        time.append(float(wordsin[len(wordsin)-3]))
     
    meantime = np.mean(time)
    meanspeed = np.mean(speed)
    stdspeed = np.std(speed) 
    meantime = round(meantime)
    meanspeed = round(meanspeed)
    stdspeed = round(stdspeed)
    print (meantime)
    print (meanspeed)
    print (stdspeed)
    sout1.close()
    generating_ouput_file(meantime,meanspeed,stdspeed)
    
def generating_ouput_file(meantime,meanspeed,stdspeed):
    outf = open('Output_file.txt','w')
    retrieved_Input_line1 = linecache.getline('Input_Data_File_For_XML.txt',2)
    Input1 = retrieved_Input_line1.strip().split(',')
    outf.write(Input1[0]+' '+Input1[1]+' '+Input1[2]+' '+str(meantime)+' '+str(meanspeed)+' '+str(stdspeed))
    print('\n')
    outf.close()
    
read_output_file_of_utility()   
    