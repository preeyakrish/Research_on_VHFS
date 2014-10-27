'''
Created on Sep 6, 2014

@author: vembu
'''
from pymongo import MongoClient
from pymongo import Connection

client = MongoClient('192.168.101.221', 27017)
db = client['makdatabase']
c = Connection('192.168.101.221', 27017)
c.drop_database('makdatabase')
