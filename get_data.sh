#!/bin/bash

# Find cookie file next to this script
COOKIE_FILE=`dirname $0`/cookie.txt
COOKIE=`cat $COOKIE_FILE`

# Generate input data url from current directory path
PTH=`echo $PWD | sed s'/.*\([0-9]\{4\}\)\/0*\([0-9]\{1,2\}\).*/\1\/day\/\2/'`
URL=https://adventofcode.com/$PTH/input

curl $URL -H "Cookie: $COOKIE" > data.txt