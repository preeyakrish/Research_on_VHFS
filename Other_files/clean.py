'''
Created on Sep 6, 2014

@author: vembu
'''

from pymongo import Connection
import os


print ("inside if condition of read write")
os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
os.system('find . -name "*.sgcf" -print0 | xargs -0 rm')
os.system('rm -rf ./chunkfile/*')
print ("removed chunkfiles")
c = Connection('localhost', 27017)
c.drop_database('makdatabase')  
