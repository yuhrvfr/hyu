#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")


-- problem after commit !!!

def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)
    print("Everything ok")
    sys.exit(0)


main()
