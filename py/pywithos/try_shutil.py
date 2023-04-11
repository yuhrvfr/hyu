#!/usr/bin/env python3
import shutil   # Utilities for Disk
import psutil   # Utilities for CPU
du = shutil.disk_usage('/')
print(du)
print("In GB total={}, used={}, free={}".format(du.total//1000000000,du.used//1000000000, du.free//1000000000) )
print("Average CPU usage percent per 0.5 second is {}".format(psutil.cpu_percent(0.5)) )

def check_disk_usage(i_disk):
    du = shutil.disk_usage(i_disk)
    freepct = du.free / du.total * 100
    print("Disk free percentage {:.2f}%".format(freepct))
    return freepct > 20

def check_cpu_usage():
    usagepct = psutil.cpu_percent(1)
    print("Percentage CPU usage is {}%".format(usagepct))
    return usagepct < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
    print("Computer is working OK!")
