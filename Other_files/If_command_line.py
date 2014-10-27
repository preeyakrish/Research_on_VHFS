'''
Created on 26-Sep-2014

@author: root
'''

from xml.etree import ElementTree
from pymongo import Connection
import os
import cmd
import subprocess

def Calling_Utility(Enableread,iteration):
    print('inside Calling_Utility')
    uout_file_name = 'utilityout.txt'
    uout = open(uout_file_name, 'a')
    wordsin = []
    itera = int (iteration)
    count = 0
    print('Iteration')
    print(itera)
    for i in range(itera):         
        cmd = './DriverTest'
        return_code = subprocess.call(cmd, stdout=uout)
        print('return_code:  %s' % return_code)        
        print("executed driver test for %s" %count)
        os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
        print("echo command")
        if (not (int(Enableread)) and not (i == itera-1)):
            print ("inside if condition of writeclean")
            os.system('find . -name "*.sgcf" -print0 | xargs -0 rm')
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
        print ("inside if condition of Enableread")
        os.system('find . -name "*.sgcf" -print0 | xargs -0 rm')
        os.system('rm -rf ./chunkfile/*')
        print ("removed chunkfiles")
        c = Connection('localhost', 27017)
        c.drop_database('makdatabase')   
        print("dropped db")    
    else:
        print ("EnablereadElseeeeeeeeee")
    print (count) 
    print ('For output check "utilityout.txt"')
    
    
def Updating_Conf_filec():
    
    Enable_write = '0'
    Enable_read = '0'
    RandomEnable = '0'
    Percentage ='0'
    
    Data_size = input("Enter the Whole Data Size in MB: ") # Assigning the values
    Block_Size = input("Enter the Block Size in Bytes: ")
    Def_Chunk_Size = input("Enter the Chunk Size in Bytes: ")
    Enable_read = input("Enable Read: ")
    if not int(Enable_read):
        Enable_write = input("Enable Write: ") 
    
    Iteration = input("Enter Iteration: ")
                      
    document = ElementTree.parse( 'conf.xml' ) # Open the input_XML_file
    root = document.getroot() # Get the root of the XML
    users = root.find( 'ChunkUtiliy' ) # Find the tag
                    
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
        user.set('RandomEnable',RandomEnable )
        user.set('Percentage', Percentage )
            
    for user in document.findall( 'ChunkUtiliy/Iteration' ):
        user.set('Count', Iteration)
                    
                    
    document.write('conf.xml') # Write into the XML file
    print ("Updated Conf file")
    Calling_Utility(Enable_read,Iteration)
Updating_Conf_filec()