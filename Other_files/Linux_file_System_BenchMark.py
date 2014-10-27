'''
Created on 24-Sep-2014

@author: root
'''

import os

def Linux_BMRK(Enable_write,Enable_Read,Block_size,Whole_data_size):
    open('speedtest','w')
    
    sample = 'write: dd if=speedtest of=./chunkfile/ddfile.txt bs=512k count=1024'
    Read = 'dd if=/chunkfile/ddfile.txt  of=speedtest bs=512k count=1024 conv=noerror'
    Enable_Read = int(Enable_Read)
    Enable_write = int(Enable_write)
    Whole_data_size = int(Whole_data_size)
    if (Enable_write):
        open('/chunkfile/ddfile.txt','w')
        cmd = ''
        cmd += 'dd if=/dev/zero of=/chunkfile/ddfile.txt bs='
        cmd += Block_size
        cmd += ' count='
        count = (int(Whole_data_size)*1024*1024)/int(Block_size)
        count = int(count)
        print (count)
        cmd += str(count)
        print(cmd)
        os.system(cmd)
    elif (Enable_Read):
        open('/chunkfile/ddfile.txt','r')
        cmd ='';
        cmd += 'dd if=/chunkfile/ddfile.txt of=test bs='
        cmd += Block_size
        cmd += ' count='
        count = (int(Whole_data_size)*1024*1024)/int(Block_size)
        count = int(count)
        print (count)
        cmd += str(count)
        cmd +=' conv=noerror'
        print(cmd)
        os.system(cmd)



Linux_BMRK('0','1','65536','512')    