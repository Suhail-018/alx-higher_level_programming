#!/bin/bash
# Takes in a URL, sendsrequest to it,then displaysizeofbodythe response
curl -sI $1 | grep 'Content-Length:' | awk '{print $2}'
