#!/bin/bash
# bash script to display status code of server

if [ -z "$1" ]; then
	echo "usage: $0 <curl>"
	exit 1
fi

curl -s -o /dev/null -w "%{http_code}" "$1"
