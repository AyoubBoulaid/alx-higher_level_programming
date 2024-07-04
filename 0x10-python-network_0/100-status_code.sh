#!/bin/bash
# bash script to display status code of server

awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
