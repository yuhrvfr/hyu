#! /usr/bin/env python3
def char_frequency(filename):
    """ counts the frquency of each character in a given file"""
    try:
        f = open(filename)
    except OSError:
        return None
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char,0)+1
    f.close()
    return characters

#print("Please enter the file name for character frquency count:")
filename = input("What is the file name you want to count char frequency: ")
if filename != None:
    ret = char_frequency(filename)
    print(ret)
