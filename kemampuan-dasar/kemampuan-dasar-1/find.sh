#!/bin/sh

for i in $(find "$1" -type f -name '*.java')
do 
    echo "Ada file Java pada direktori $i"
done