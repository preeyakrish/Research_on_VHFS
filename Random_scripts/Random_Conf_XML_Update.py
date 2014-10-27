'''
Created on Sep 13, 2014

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
import Random_Utility_call as cal


def Updating_Conf_filef(ifile1,EnableRandom2,Iteration2):
    
    with open(ifile1, 'r') as f: # Opening the Input_Data_file in read mode
        data = f.readlines()
        lno = 0
        # Read line by line
        for line in data:
            print('inside for line in data')
            lno = lno + 1
            words = line.strip().split(",") # Splitting the data values
            print (words[0],words[1],words[2]) # For Debugging
            Data_size = words[0] # Assigning the values
            Block_Size = words[1]
            Def_Chunk_Size = words[2]
            Enable_read = words[3]
            Enable_write = words[4]  
            RandomEnabl1e = EnableRandom2
            Iteration = Iteration2
            seedvalu1e = str(random.randrange(0,50000))
            
            if int(Enable_read):
                print ('inside if int(Enable_read):')
                read_xml(Data_size,Block_Size,Def_Chunk_Size,Enable_read,Enable_write,RandomEnabl1e,Iteration,seedvalu1e,ifile1,lno)
            else: 
                print('inside if int(Enable_read): else:else:')
                write_xml(Data_size,Block_Size,Def_Chunk_Size,Enable_read,Enable_write,Iteration,ifile1,lno)
        f.close()
 
def read_xml(Data_size,Block_Size,Def_Chunk_Size,Enable_read,Enable_write,RandomEnabl1e,Iteration,seedvalu1e,ifile1,lno):
    percentage = 0
    while (percentage <=100):
        print('inside read_xml') 
        print('percentage')
        print(percentage)  
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
            user.set('Percentage', str(percentage))
            user.set('Seed', seedvalu1e)
        
        for user in document.findall( 'ChunkUtiliy/Iteration' ):
            user.set('Count', Iteration)           
            
        document.write('conf.xml') # Write into the XML file
        print ("Updated Conf file")
        print (lno)
        uout_file_name = 'utilityout.txt'
        open_file = open(uout_file_name,'w')
        open_file.write("read_xmlread_xml in Conf_xml_file inside")
        open_file.close()
        print('b4 cal.Calling_Utility')
        cal.Calling_Utility(Enable_read, Iteration,ifile1,lno)
        percentage = percentage + 20

        
def write_xml(Data_size,Block_Size,Def_Chunk_Size,Enable_read,Enable_write,Iteration,ifile1,lno):
    print ("inside if condition of read_xml")
    os.system('rm -rf ./chunkfile/*')
    print ("removed read_xmlchunkfiles")
    c = Connection('localhost', 27017)
    c.drop_database('makdatabase')   
    print("dropped read_xmldb")
    print(Iteration)
    print ('inside write_xmlwrite_xml ')
    Iteration = '1'
    print('after assingin iteration00')
    print(Iteration)
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
    
    for user in document.findall( 'ChunkUtiliy/Iteration' ):
        user.set('Count', Iteration)           
        
    document.write('conf.xml') # Write into the XML file
    print ("Updated Conf file")
    print (lno)
    uout_file_name = 'utilityout.txt'
    open_file = open(uout_file_name,'w')
    open_file.write("Write write_xmlin Conf_xml_file inside")
    open_file.close()
    print('b4 Calling_Utility in write_xml')
    cal.Calling_Utility(Enable_read, Iteration,ifile1,lno)

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
    Iteration = ''
    ifile = ''
    try:
        opts, args = getopt.getopt(argv,"h,c,f,r:i:t:",["EnableRandom=","Iteration=","iFile="])
    except getopt.GetoptError:
        print ('Random_Conf_XML_Update.py -f or -c')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Random_Conf_XML_Update.py -f or -c')
            sys.exit(2)
        elif opt == '-c':
            #print ('Fresh_Utility.py -d <Whole_Data in MB> -b <Block_size in Bytes> -s <Chunk_Size in Bytes> -er <Enable Write> -ew <Enable_Read> -r <Enable_Random> -p <percentage> -i <iteration>')
            Updating_Conf_filec()
        elif opt == '-f':
            print ('Random_Conf_XML_Update.py -t <Input_File> -r <Enable_Random> -i <iteration>')
            sys.exit(2)
        elif opt in ('-t', "--iFile"):
            ifile = arg        
        elif opt in ("-r", "--EnableRandom"):
            EnableRandom = arg
        elif opt in ("-i", "--Iteration"):
            Iteration = arg
      
    Updating_Conf_filef(ifile,EnableRandom,Iteration)     
    
if __name__ == "__main__":
    main(sys.argv[1:])
        
        