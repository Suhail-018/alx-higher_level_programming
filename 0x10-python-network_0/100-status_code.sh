#!/bin/bash
# Sends a requesttoaURL passedasan arg,displaysonlystatuscodeof the response
curl -so /dev/null -w %{http_code} $1
