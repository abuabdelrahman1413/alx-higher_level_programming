#!/bin/bash
# script print the status code of a request
curl "${1}" -s -w "%{http_code}" --output /dev/null
