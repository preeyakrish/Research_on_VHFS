'''
Created on 14-Oct-2014

@author: root
'''
#!/usr/bin/python
import os
import cmd
import subprocess

def VMplayer(file_name):
    uout = open('pingfile.txt', 'a')
    true = True
    #cmd = 'vmrun -T player start /path/to/vm/my.vmx'
    #os.system(cmd)
    while not true:
        cmd = 'ping -n 1 192.168.103.220'
        subprocess.call(cmd, stdout=uout)
        #os.system('ping 192.168.103.220')
        for lines in uout.readlines():
            word = lines.strip().split(' ')
            
        
    

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
    VMplayer(file_name)

def construct_line():
    print('construct_line')
    fopen = open('list_of_vhd_files.txt','r')
    for lines in fopen.readlines():
        lines = lines.strip()
        text = 'ide0:0.fileName = "' + str(lines) + str('"') + "\n"
        print(text)
        replace_line("vfx.txt", 51, text)
    fopen.close()
  
construct_line()
        