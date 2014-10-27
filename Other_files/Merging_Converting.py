'''
Created on Sep 6, 2014

@author: vembu
'''
import linecache

merge_file = open('merge.txt','w+')

"""with open('Testing_Input_for_Read_Write.txt','r') as inp:
    with open('Testing_output_file.txt','r') as out:
        data_inp = inp.readlines()
        data_out = out.readlines()"""
        
for i in range(1,40):
    if (i%2 == 0):
        print ("Do nothing")
    else:
        retrieved_Input_line = linecache.getline('Testing_Input_for_Read_Write.txt', i)
        Input = retrieved_Input_line.strip().split(',')
        retrieved_Output_line = linecache.getline('Testing_output_file.txt',i)
        output = retrieved_Output_line.strip().split('\t')
        merge_file.write(Input[0] + "\n")
       
#       for inp_line in data_inp
 #           words = inp_line.strip().split(",")
  ##         if (Write_enable) == 1:
    #            merge_file.write(inp_line)"""
            
            
