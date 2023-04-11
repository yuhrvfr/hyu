#!/usr/bin/env python3
import csv
import os

fn = "st_csv.txt"
ft = "st_csv_n.txt"
f= open(fn,'r')
if os.path.exists(ft):
    os.remove(ft)

f1 = open(ft,'a')
for l_line in f:
    #print(str(len(l_line)))
    f1.write(l_line[:-3]+'\n')
f.close()
f1.close()

fn="st_csv_n.txt"
f= open(fn)
csv_f = csv.reader(f)
for idx, row in enumerate(csv_f):
    if idx == 0:
        label = row
    else:
        sym,desc,qty,price,begVal,endVal,cost = row
        print('{} quantity={}, Price={}, BegVal={}, EndVal={}, Cost={}'.format(sym,qty,price,begVal,endVal,cost))

f.close()

list2csv = [['myworkstation.local','192.168.25.46'],['webser.cloud','10.2.5.6']]
with open("hosts.csv","w") as l_file:
    writer = csv.writer(l_file)
    # writer.writerows(list2csv)
    for row in list2csv:
        writer.writerow(row)


print('-------------------')

def gainLoss(i_worth,i_cost):
    try:
        lw = float(i_worth)
        lc = float(i_cost)
        return float("{:.2f}".format(lw-lc))
    except ValueError:
        return 0


#CSV Dict reader

fn='st_csv_n.txt'
#fn='hosts.csv'

with open(fn) as file:
    reader = csv.DictReader(file)
    gl = 0
    for row in reader:
        # print(row)
        print('{:>6}:own {}, worth {}, costed {}, g/l {}'.format(row["Symbol"],
        row["Quantity"],row["Ending Value"],row["Cost Basis"],
        gainLoss(row["Ending Value"],row["Cost Basis"])))
        gl += gainLoss(row["Ending Value"],row["Cost Basis"])
    print(gl)


print("=====================")

myDict=[]
label=[]

with open(fn) as file:
    reader = csv.DictReader(file)
    for row in reader:
        myDict.append(row)

with open(fn) as file:
    csv_f = csv.reader(file)
    for idx, row in enumerate(csv_f):
        if idx == 0:
            label = row

print(label)
print(myDict)

with open("writeDic2csv.csv","w") as file:
    writer = csv.DictWriter(file,fieldnames=label)
    writer.writeheader()
    writer.writerows(myDict)


print("==========================")

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
print(contents_of_file("flowers.csv"))

print('-------------------------')

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    for row in rows:
      name, color, type = row
      # Format the return string for data rows only
      if name != "name" and color != "color" and type != "type":
          return_string += "a {} {} is {}\n".format(color,name,type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
