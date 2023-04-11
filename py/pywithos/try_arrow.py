#!/usr/bin/env python3
# This is a shebang example


import arrow

myDate = arrow.get('20230404','YYYYMMDD')

print(myDate)

myDate.shift(weeks = 6).format('MMM-DD-YYYY')

print(myDate.format('MMM-DD-YYYY'))
print(myDate.shift(weeks = 6).format('MMM-DD-YYYY'))
print(myDate.format('MMMM-DD-YYYY'))
