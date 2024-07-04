#!/usr/bin/env bash
# script sends a request to url and display the size of the body of the response
curl -s "$1" | wc -c
