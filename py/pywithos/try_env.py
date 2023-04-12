#! /usr/bin/env python3
import os

print("HOME: {}".format(os.environ.get('HOME','')))
print("SHELL: {}".format(os.environ.get('SHELL','')))
print("FRUIT: {}".format(os.environ.get('FRUIT','')))
