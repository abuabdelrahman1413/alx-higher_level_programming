#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -sX POST -d "email=5Z9bI@example.com&subject=I will always be here for PLD" "$1"
