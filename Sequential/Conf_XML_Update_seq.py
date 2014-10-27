'''
Created on Sep 3, 2014

@author: vembu
'''
from xml.etree import ElementTree
from pymongo import Connection
import numpy as np
import subprocess
import os
import cmd
import sys, getopt
import random
import Calling_Utiltiy_seq as cal


def Updating_Conf_filef(ifile1,Iteration2):
    
    with open(ifile1, 'r') as f: # Opening the Input_Data_file in read mode
        data = f.readlines()
        lno = 0
        # Read line by line
        for line in data:
            lno = lno + 1
            words = line.strip().split(",") # Splitting the data values
            print (words[0],words[1],words[2]) # For Debugging
            Data_size = words[0] # Assigning the values
            Block_Size = words[1]
            Def_Chunk_Size = words[2]
            Enable_read = words[3]
            Enable_write = words[4]  
            RandomEnabl1e = '0'
            Percentag1e = '0'
            Iteration = Iteration2
            seedvalu1e = str(random.randrange(0,50000))
                  
            document = ElementTree.parse( 'conf.xml' ) # Open the input_XML_file
            membership = document.getroot() # Get the root of the XML
            users = membership.find( 'ChunkUtiliy' ) # Find the tag
            
            for user in document.findall( 'ChunkUtiliy/Write' ): # Set the values of data file to XML attributes
                user.set('BlockSize', Block_Size)
                user.set('DataToWriteMB',Data_size )
                user.set('EnableWrite',Enable_write )
                
            for user in document.findall( 'ChunkUtiliy/Read' ): # Set the values of data file to XML attributes
                user.set('DataToReadMB',Data_size )
                user.set('EnableRead',Enable_read )            
        
            for user in document.findall( 'ChunkUtiliy/Chunk' ):# Set the values of data file to XMl attributes
                user.set('ChunkSize', Def_Chunk_Size)
            
            for user in document.findall( 'ChunkUtiliy/RandomRead' ):# Set the values of data file to XMl attributes
                user.set('RandomEnable',RandomEnabl1e )
                user.set('Percentage', Percentag1e )
                user.set('Seed', seedvalu1e)
            
            for user in document.findall( 'ChunkUtiliy/Iteration' ):
                user.set('Count', Iteration)
                
                
            document.write('conf.xml') # Write into the XML file
            print ("Updated Conf file")
            print (lno)
            uout_file_name = 'utilityout.txt'
            open_file = open(uout_file_name,'w')
            open_file.write("Hiiiiiiiiiiiiiiiiiii in Conf_xml_file inside")
            open_file.close()
            cal.Calling_Utility(Enable_read, Iteration,ifile1,lno)
        f.close()
        
        

def Updating_Conf_filec():
    
    Data_size = input("Enter the Whole Data Size in MB: ") # Assigning the values
    Block_Size = input("Enter the Block Size in Bytes: ")
    Def_Chunk_Size = input("Enter the Chunk Size in Bytes: ")
    Enable_read = input("Enable Read: ")
    Enable_write = input("Enable Write: ") 
    RandomEnabl1e = input("Enable Random Read: ")
    if int(RandomEnabl1e) == 1:
        Percentag1e = input("Enter the percentage of random: ")
    Iteration = input("Enter Iteration: ")
    seedvalu1e = str(random.randrange(0,50000))
                      
    document = ElementTree.parse( 'conf.xml' ) # Open the input_XML_file
    membership = document.getroot() # Get the root of the XML
    users = membership.find( 'ChunkUtiliy' ) # Find the tag
                
    for user in document.findall( 'ChunkUtiliy/Write' ): # Set the values of data file to XML attributes
        user.set('BlockSize', Block_Size)
        user.set('DataToWriteMB',Data_size )
        user.set('EnableWrite',Enable_write )
                    
    for user in document.findall( 'ChunkUtiliy/Read' ): # Set the values of data file to XML attributes
        user.set('DataToReadMB',Data_size )
        user.set('EnableRead',Enable_read )            
            
    for user in document.findall( 'ChunkUtiliy/Chunk' ):# Set the values of data file to XMl attributes
        user.set('ChunkSize', Def_Chunk_Size)
                
    for user in document.findall( 'ChunkUtiliy/RandomRead' ):# Set the values of data file to XMl attributes
        user.set('RandomEnable',RandomEnabl1e )
        user.set('Percentage', Percentag1e )
        user.set('Seed', seedvalu1e)
                
    for user in document.findall( 'ChunkUtiliy/Iteration' ):
        user.set('Count', Iteration)
                    
                    
    document.write('conf.xml') # Write into the XML file
    print ("Updated Conf file")
    
    cal.Calling_Utility(Enable_read, Iteration)
    

    
def main(argv):
    EnableRandom = ''
    Percentage = ''
    Iteration = ''
    ifile = ''
    try:
        opts, args = getopt.getopt(argv,"h,c,f,i:t:",["Iteration=","iFile="])
    except getopt.GetoptError:
        print ('Conf_XML_Update_seq.py -f or -c')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Conf_XML_Update_seq.py -f or -c')
            sys.exit(2)
        elif opt == '-c':
            #print ('Fresh_Utility.py -d <Whole_Data in MB> -b <Block_size in Bytes> -s <Chunk_Size in Bytes> -er <Enable Write> -ew <Enable_Read> -r <Enable_Random> -p <percentage> -i <iteration>')
            Updating_Conf_filec()
        elif opt == '-f':
            print ('Conf_XML_Update_seq.py -t <Input_File> -i <iteration>')
            sys.exit(2)
        elif opt in ('-t', "--iFile"):
            ifile = arg        
        elif opt in ("-i", "--Iteration"):
            Iteration = arg
      
    Updating_Conf_filef(ifile,Iteration)     
    
if __name__ == "__main__":
    main(sys.argv[1:])
        
        