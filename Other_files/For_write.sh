#!/bin/bash
myfile = ./scripting.txt
for i in {1..10}
do
sync;sync;sync;echo 3 > /proc/sys/vm/drop_caches
dd if=/dev/zero of=$myfile bs=512M count=100  
done