#!/bin/bash
# Takes in aURLasanarg,sends a GET requesttoURL,displaybody of the response
arg = $1
curl -sH "X-School-User-Id: 98" arg
