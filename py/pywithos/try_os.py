#!/usr/bin/env python3
import os
import datetime

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

if os.path.exists("guests.txt"):
    os.rename("guests.txt","guests1.txt")

if os.path.exists("guests.txt"):
    print("{} file exists".format("guests.txt"))
else:
    print("{} file does not exist".format("guests.txt"))


if os.path.exists("guests1.txt"):
    lf = "guests1.txt"
    print("{} file exists and it will be deleted".format(lf))
    # os.copy("guests1.txt","guests2.txt")
    lsizeinbyte = os.path.getsize(lf)
    print(lsizeinbyte)

    lunixtimestamp = os.path.getmtime(lf)
    print(str(lunixtimestamp))

    ldt = datetime.datetime.fromtimestamp(lunixtimestamp)
    print(ldt)

    print(os.path.exists(lf))
    print(os.path.isfile(lf))
    lfp = os.path.abspath(lf)
    print(lfp)
    os.remove(lf)
    print(os.path.isfile(lf))
