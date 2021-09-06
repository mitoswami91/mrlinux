#!/bin/bash
for N in {10..5..} # change later if it works fast enough
do
echo $N' sec'
env sleep 5
done

echo ' /timeout 10sec/ or [ctrl][c]'
read -t 10
rdesktop 80.0.0.139 -u -p -x:l  
