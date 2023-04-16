#!/usr/bin/env python3
import sys
import re

pattern = r'USER \([\w|\s]+\)$'
pattern1 = r'USER \((\w+)\)$'
pattern2 = r'^Jul [\w|\s]+:$'
pattern3 = r'Jul [0-9]+ [0-9]+:[0-9]+:[0-9]+'  #:[0-9]+:[0-9]+
pattern4 = r'\[[0-9]+\]'
pattern5 = r'(Jul [0-9]+ [0-9]+:[0-9]+:[0-9]+).*(\[[0-9]+\])' #multi groups filtering

l = "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"
l1 = "Jul 04 20:20:30 computer.xyz CRON[240]: USER (this is the user)"
l2 = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
l3 = "Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""
#  Jul 6 14:03:40 pid:29807

res3 = re.search(pattern1,l2)
print(res3.group(0))
print(res3.group(1))

res4 = re.search(pattern4,l3)
print(res4.group(0).translate({ord(i): None for i in '[]'}))
print(type(res4.group(0)))
print("{} pid:{}".format(res3.group(0),res4.group(0)))

res =re.search(pattern5,l3)
print('--------------')
print(res.group(0))
print(res.group(1))
print(res.group(2))
print('--------------')
print("{} pid:{}".format(res.group(1),res.group(2).translate({ord(i): None for i in '[]'})))





import re
def show_time_of_pid(line):
  pattern = r'(Jul [0-9]+ [0-9]+:[0-9]+:[0-9]+).+(\[[0-9]+\])'
  result = re.search(pattern, line)
  return "{} pid:{}".format(result.group(1),result.group(2).translate({ord(i): None for i in '[]'}))

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

# logfile = sys.argv[1]
# with open(logfile) as file:
#     for line in file:
#         if not "CRON" in line:
#             continue
#         pattern = r'USER \([\w|\s]+\)$'
#         result = re.search(pattern,line)
#         print(result[1])
