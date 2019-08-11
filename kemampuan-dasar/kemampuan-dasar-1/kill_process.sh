#!/bin/bash

if  pgrep -x "$1" > /dev/null 
then
    kill $(ps aux | grep $1 | awk '{print $2}')
else
    echo "service not found or already terminated"
fi