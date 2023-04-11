#!/usr/bin/env python3
l_file = open("app.py")
print('read first line: '+l_file.readline())
print('--------')
print('read the rest: '+l_file.read())
l_file.close()  #Don't forget to close the file if I open it with open(<file>)

print('+=======+')
# with open(<file>) as file instruction with close the file automatically.
# with method restriict a single bloc of code
with open('app.py') as l_file:
    print(l_file.read())



with open('app.py') as l_file:
    txt = l_file.read()
    i = 0
    for line in txt:
        # PAS BON txt est une string donc line est un caractere
        i += 1
        print(str(i) +": "+ line)

# Pour lire par  ligne
with open("module.py") as l_file:
    for idx, line in enumerate(l_file):
        if 'print' in line:
           print("end: " + str(idx)+ " "+ line.upper(),end="")
           print("strp: " + line.upper().strip())

# Pour lire the text entier et product une list of strings
l_file= open("module.py")
l_lines = l_file.readlines()
l_file.close()
print(l_lines)
l_lines.sort()

for idx, l in enumerate(l_lines):
    if 'print' in l:
        print(str(idx) + " : "+l)

print(l_lines)
print(type(l_lines))
