text = 'il a mange beaucoup de chocolat'
ntext = text
for a in text:
    if a == ' ':
        i = ntext.index(a)
        print('space position: ',i)
        ntext=ntext[:i]+'-'+ntext[i+1:]
print(text)
print(ntext)

ntext = ntext.replace('-','*')
print(ntext)

ntext = ntext.split('*')
print(ntext)

ntext[0]='#'.join(ntext)
mtext = ntext[0]
print(ntext)
print(mtext)

print(mtext.isnumeric())
print(mtext.isalpha())
mtext = mtext.replace('#',' ')
print(mtext)
print(mtext.isalpha())
mtext = mtext.replace(' ','')
print(mtext)
print(mtext.isalpha())

def reverseStr(input_string):
    new_string = input_string.upper().replace(' ','')
    print(new_string)
    reverse_string = ""
    for letter in range(len(new_string)-1,-1,-1):
        if letter != " ":
            reverse_string = reverse_string + new_string[letter]
    return reverse_string

print(reverseStr("Hello Papa Tango Charly"))
