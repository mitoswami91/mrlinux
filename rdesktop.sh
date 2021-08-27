#!/bin/bash

#Resolve hostname in linux 
echo $(hostname -I | cut -d\  -f1) $(hostname) | sudo tee -a /etc/hosts
sudo apt-get update -y && sudo apt-get install rdesktop -y && rdesktop
#/etc/apt/sources.list

#
## EOL upgrade sources.list
# deb http://old-releases.ubuntu.com/ubuntu/ precise main restricted universe multiverse
# deb http://old-releases.ubuntu.com/ubuntu/ precise-updates main restricted universe multiverse
# deb http://old-releases.ubuntu.com/ubuntu/ precise-security main restricted universe multiverse
