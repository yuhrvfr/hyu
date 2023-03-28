file_c ={'jpg':10,'txt':12,'png':33}
for ext,cnt in file_c.items():
   print('there are {amt} files .{ex}.'.format(amt=cnt,ex=ext))
print(file_c.keys())
print(file_c.values())

file_c['doc'] = 66
file_c['jpg'] = 13
print(file_c)

print('txt' in file_c)
print(file_c.items())

for value in file_c.values():
    print(value)

def cnt_letters(text):
    result ={}
    for letter in text:
        if letter not in result:
            result[letter]= 0
        result[letter] += 1
    return result

print(cnt_letters('aaaaa'))
print(cnt_letters('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))

d = {'Long_text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
'Short_text':'Very short.'}

print(d)


CountryCities={'USA':['San Francisco','New York'], 'France':['Paris','Lyon'],  'China':['Beijing','Shanghai'], 'Germany':['Berlin', 'Stuttgat']}

print(CountryCities)

print(CountryCities.get('Maroc','Nothing Found'))
print(CountryCities.get('USA','Nothing Found'))

CountryCities['USA'].append('Chicago')
print(CountryCities.get('USA','Nothing Found'))

OtherCities={'France':'Lourdes', 'UK':'London'}
CountryCities.update(OtherCities)
print(CountryCities)


def network(servers):
    result = ""
    for hostname, IP_address in servers.items():
        result += "The IP address of the {} server is {}".format(hostname, IP_address) + "\n"
    return result

print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))

genre = "transcendental"
print(genre[:-1])
print(genre[:-2])
print(genre[:-3])
print(genre[:-4])
print(genre[:-5])
print(genre[:-6])
print(genre[:-7])
print(genre[:-8])
print(genre[-7:9])

#transc
#nd

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

print(colors)
