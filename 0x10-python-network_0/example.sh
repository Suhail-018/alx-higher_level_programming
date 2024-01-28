#!/bin/bash
URL=$1
SIZE=$(curl -I "$URL" | grep -i "content-length" | awk '{print $2}')
echo "$SIZE"
