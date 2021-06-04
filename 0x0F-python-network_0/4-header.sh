#!/bin/bash
# send get request with ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
curl -sH "X-HolbertonSchool-User-Id":98 "$1"
