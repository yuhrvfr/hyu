#!/usr/bin/env python3
import sys
print(sys.argv)


import os
import sys

filename = sys.argv[1]
if not os.path.exists(filename):
    with open(filename,'w') as file:
        file.write("New file creation\n")
else:
    print("Error, the file {} already exists".format(filename))
    sys.exit(1)
