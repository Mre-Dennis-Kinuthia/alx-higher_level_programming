#!/bin/bash

# Take in the URL as the first argument
url="$1"

# Use curl to send a request and store the response body in a variable
response=$(curl -sI "$url" | grep -i 'content-length' | awk '{print $2}')

# Display the size of the response body in bytes
echo "$response"