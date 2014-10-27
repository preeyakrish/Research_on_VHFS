'''
Created on Sep 3, 2014

@author: vembu
'''
from xml.etree import ElementTree
from pymongo import Connection
import os
import cmd
import File_Plot_Graph

def main():
    with open('Input_for_Read_Write.txt', 'r') as f: # Opening the Input_Data_file in read mode
        data = f.readlines() # Read line by line
        count = 0
        for line in data:
            words = line.strip().split(",") # Splitting the data values
            print (words[0],words[1],words[2]) # For Debugging
            Data_size = words[0] # Assigning the values
            Block_Size = words[1]
            Def_Chunk_Size = words[2]
            Enable_read = words[3]
            Enable_write = words[4]
            
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
       
            document.write('conf.xml') # Write into the XML file
            print ("Updated Conf file")
            cmd = 'time ./BulkInsert' # Run the Utility with the given input
            os.system(cmd)
            print("executed driver test")
            os.system('echo 3 > /proc/sys/vm/drop_caches')
            print("echo command")
            count = count + 1
            print ('%s experiment done' %(count))
            if int(Enable_read):
                print ("inside if condition of read write")
                os.system('rm -rf ./chunkfile/*')
                print ("removed chunkfiles")
                c = Connection('localhost', 27017)
                c.drop_database('makdatabase')   
                print("dropped db")    
            else:
                print ("Elseeeeeeeeee")   
                       
    f.close()
    
main()



        
        