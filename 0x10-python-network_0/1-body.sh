#!/bin/bash                                                                   
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response                                                  
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then curl -sL "$1"; fi
