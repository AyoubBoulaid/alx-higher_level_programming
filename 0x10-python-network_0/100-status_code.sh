#!/bin/bash
# bash script to display status code of server

curl -o /dev/null -sw "%{http_code}" $1
