#!/bin/bash
n=1
# while test $n -le 5; do
#   echo "Iteration number $n"
#   ((n+=1))
# done

while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done
