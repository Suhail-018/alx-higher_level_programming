#!/bin/bash
# Takes in a URL and displays all HTTP methodstheserver will accept
curl -sI $1 | grep Allow: | cut -d " " -f 2-
