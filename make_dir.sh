#!/bin/bash

if [ -z $1 ]
then
    echo "Usage: make_dirs.py <dir_name>"
    exit
fi

mkdir -p $1
cp ../aoc.py $1
touch $1/data.txt
touch $1/test.txt
