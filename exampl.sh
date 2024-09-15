#!/bin/bash

#author: amol
#date: 12/12/2012

set -x

echo "Print disk space"
df -h

#create a directory
mkdir gitdir

#change to gitdir
cd gitdir

#create 2 file
touch 1.py 5.py
