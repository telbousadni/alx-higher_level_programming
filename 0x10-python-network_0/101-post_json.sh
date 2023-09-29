#!/bin/bash
# Takes a URL and sends a request to it and displays the status code of the response
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
