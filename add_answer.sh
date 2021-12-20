#!/bin/bash

# Find cookie file next to this script
COOKIE_FILE=`dirname $0`/cookie.txt
COOKIE=`cat $COOKIE_FILE`

PTH=`echo $PWD | sed s'/.*\([0-9]\{4\}\)\/0*\([0-9]\{1,2\}\).*/\1\/day\/\2/'`
DAY=`echo $PWD | sed s'/.*\([0-9]\{4\}\)\/0*\([0-9]\{1,2\}\).*/\2/'`
DAY=$[DAY+1]
URL=https://adventofcode.com/$PTH
VAL=`curl $URL -H "Cookie: $COOKIE" 2>/dev/null | grep -o '<p>Your puzzle answer was <code>.*</code>' | grep -o -E '[0-9]+' | tr '\n' ' ' | sed 's/\([0-9]\+\) \([0-9]\+\)/\[ \1, \2\ ]/'`

if [ ! -f ../answers.json ]
then
    echo [ >> ../answers.json
    for i in `seq 1 24` 
    do
        echo '    [ ],' >> ../answers.json
    done
    echo '    [ ]' >> ../answers.json
    echo ] >> ../answers.json
fi

sed -i $DAY's/\[.*\]/'"$VAL"'/' ../answers.json