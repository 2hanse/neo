#!/bin/bash

i=1
cnt=$1

while [ $i -le $cnt ]; do
    let uid+=1
    useradd -u $uid -g users -d /home/user$i -s /bin/bash -m user$i
    passwd -d user$i
    let i+=1
done
echo Complete!!
