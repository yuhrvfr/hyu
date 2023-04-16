#!/bin/bash
for fruit in orange apple grapes; do
  echo I like $fruit
done;

for file in *.txt; do
  name=$(basename "$file" .txt)  #$( OScommand  surrounding filename with "" for cases filename has some spaces)
  tmp=${name:0:4}
  #echo $tmp
  bash="bash"
  if [ "$tmp" = "$bash" ]; then
    #echo mv "$file" "$name".lst  Always use echo to verify the instruction the script perform before executing
    mv "$file" "$name".lst
  else
    #echo mv "$file" bash_"$name".lst
    mv "$file" bash_"$name".lst
  fi
done;
