#!/bin/bash
# script send json to url
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
