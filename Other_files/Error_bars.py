'''
Created on Sep 9, 2014

@author: vembu
'''
"""fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
ax = axs[0,0]
ax.errorbar(x, y, yerr=yerr, fmt='o')
ax.set_title('Vert. symmetric')"""
'''import subprocess
import os
p = os.system('ipconfig')
print (p)

proc=subprocess.Popen('ipconfig', shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]
print (output)'''
import subprocess
import linecache
import numpy as np

cmd = ['ipconfig']
sword = '-DBTIME'
o = open('ooo.txt','w')
out = open('outputrand.txt', 'r')
wordsin = []
speed = []
    #return_code = subprocess.call(cmd, stdout=out)
    #print(return_code)
alllines = out.readlines()
for sline in alllines:
    if sline.startswith('-DBTIME'):
        o.write(sline)
        wordsin = sline.strip().split(' ')
        speed.append(float(wordsin[len(wordsin)-1]))
print (len(speed)) 
     
print (np.std(speed))
print (np.mean(speed))


out.close()
o.close()            
        
            
            
        
    
    
    
   