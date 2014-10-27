'''
Created on Sep 9, 2014

@author: vembu
'''
 
import os.path

def Check_in_out_file():
    output_file_name = 'Output_file.txt'
    Input_file_name = '50GB-Input.txt'
    print (os.path.isfile(output_file_name))
    if (os.path.isfile(output_file_name)):
        output_file_lines = file_total_lines(output_file_name)
        Input_file_lines = file_total_lines(Input_file_name)
        print (output_file_lines)
        print (Input_file_lines)
        if Input_file_lines != output_file_lines :
            
    

def file_total_lines (file_name):
    ofile = open(file_name,'r')
    file = ofile.readlines()
    count = 0
    for i in file:
        count +=1
    print (count)
    return count

Check_in_out_file()