#!/usr/bin/env python3
from simple_fct2test import *
import os
import sys

def main():
    filename = sys.argv[1]

    # if not os.path.exists(filename):
    #     print("{} does not exist in the current directory".format(filename))
    #     sys.exit(1)

    formattext(filename)

main()
