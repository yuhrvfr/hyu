#!/usr/bin/env python3
import re
import os
import shutil

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result == None:
        return name #return empty string for empty arguments
    return "{} {}".format(result[2], result[1])
    #return "{} {}".format(result.group(2), result.group(1))


#print(rearrange_name('Herve, Yu'))

def remove_digit(text):
    assert type(text) == str, "remove_digit input must be a string"
    print(len(text))
    if len(text) == 0:
        raise ValueError("remove_digit input must not be empty")
    res = ''
    for i in range(len(text)):
        if not text[i].isnumeric():
            res = res + text[i]
        elif text[i] == '2':
            res = res + ' to '
        elif text[i] == '4':
            res = res + ' for '
        else:
            res = res + ' '
    return res

#print(remove_digit('Test4Fin2Pie'))

def file_start_with(filename,fsw):
    l = len(fsw)
    s = filename[:l]
    if fsw == s:
        return True
    return False

def mk_new_dir(dir,emptyRequired):
    if emptyRequired == None:
        emptyRequired = 'N'
    ldir = dir
    i = 0
    lc = 'N'
    while os.path.isdir(ldir):
        if emptyRequired.upper() == "Y":
            lf = os.listdir(os.path.join('.',ldir))
            if len(lf) != 0:
                ldir = ldir + str(i)
                i += 1
                lc = 'Y'
            else:
                print('{} directory is empty hence can be used'.format(ldir))
                lc = 'N'
                break
        else:
            print('{} directory exists no requirement to be empty'.format(ldir))
            break
    if lc == 'Y':
        print("{} directory is created".format(ldir))
        os.mkdir(ldir)
    return ldir


def mv_dir_file(dir, fsw):
    #Check if dir exists
    ldir = mk_new_dir(dir)

    lf = os.listdir('.')
    for elt in lf:
        if file_start_with(elt,fsw) and not os.path.isdir(elt):
           lfc = os.path.join('.',elt)
           lfd = os.path.join(os.path.join('.',ldir),elt)
           shutil.move(lfc,lfd)
           print("The file {} will be moved to {}".format(lfc,lfd))
