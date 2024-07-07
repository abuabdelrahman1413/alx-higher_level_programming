#!/bin/bash
# script send json to url
curl -sX POST -H "Content-Type: application/json" -d @"$(basename "$2")" "$1"