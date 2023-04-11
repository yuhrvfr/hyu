#!/usr/bin/env python3
import os

mycwd = os.getcwd()
print(mycwd)

ld = "new_dir"

if os.path.isdir(ld):
    print("{} directory exists".format(ld))
else:
    os.mkdir(ld)

os.chdir(ld)

lf = "newfile.txt"
with open(lf,"w") as l_file:
    l_file.write("this is a file.")

# os.remove(lf)
#
# mycwd = os.getcwd()
# print(mycwd)

os.chdir("..")

os.remove(os.path.join(ld,lf))
os.rmdir(ld)

# mycwd = os.getcwd()
# print(mycwd)
#
# os.rmdir(ld)


dir = "."
listelt = os.listdir(dir)

for elt in listelt:
    fullname = os.path.join(dir,elt)
    if os.path.isdir(fullname):
        print("{} is a directory".format(os.path.abspath(fullname)))
    else:
        print("{} is a file".format(fullname))

print(listelt)


def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename,"w") as file:
    pass

  # Return the list of files in the new directory
  os.chdir("..")
  if os.path.isdir(directory):
      print("{} is a directory.".format(directory))
      return os.listdir(directory)
  elif os.path.isdir(os.path.join(os.getcwd(),directory)):
      print("{} needs to append with cwd".format(os.path.join(os.getcwd(),directory)))
      return os.listdir(os.path.join(os.getcwd(),directory))
  return(os.listdir("new_dir"))


print(new_directory("PythonPrograms", "script.py"))

os.remove(os.path.join("PythonPrograms","script.py"))
os.rmdir("PythonPrograms")



import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,"w") as file:
    pass
  timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
  # Convert the timestamp into a readable format, then into a string
  #___
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  # print(type(timestamp.strftime('%Y-%m-%d %H:%M:%S')))
  return ("{}".format(timestamp.strftime('%Y-%m-%d')))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd



import os
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  relative_parent = os.path.join("..", ".")
  print(relative_parent)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())

def str_beg_try(name):
    if 'try_' in name:
        if name.index('try_')==0 and ".py" in name:
           return True
    return False

import shutil

if not os.path.isdir('pywithos'):
    os.mkdir('pywithos')
lf = os.listdir('.')
for elt in lf:
    if str_beg_try(elt):
        lfc = os.path.join('.',elt)
        lfd = os.path.join(os.path.join('.','pywithos'),elt)
        shutil.move(lfc,lfd)
        print("The file {} will be moved to {}".format(lfc,lfd))
