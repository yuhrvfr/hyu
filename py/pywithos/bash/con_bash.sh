#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
  echo "Everything is ok localhost is present"
else
  echo "ERROR! 127.0.0.1 ie localhost is not in /etc/hosts"
fi
