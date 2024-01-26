#!/bin/bash
# Takes in aURLsendsaPOSTrequesttopassed URL,displaysbody of the response
arg = $1
curl -sd "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" arg
