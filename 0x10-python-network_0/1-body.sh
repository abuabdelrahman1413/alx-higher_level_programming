#!/bin/bash
#  script that takes in a URL, sends a GET request to the URL, and displays the body of the response Display only body of a 200 status code response.
http_response=$(curl -s -o response.txt -w "%{response_code}" $"1")
g
