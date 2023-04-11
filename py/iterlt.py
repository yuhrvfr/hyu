l = [('herve','yu',1966), ('weizhen','huang',1967),('gabrielle marthe','yu',2000),('joseph','yu',2003)]

for elt in l:
    print('{:<10}, {:<20} born in {}'.format(elt[1],elt[0],elt[2]))

for pren, nom, an in l:
    print(str(an)+' - '+nom+' - '+pren)

for index, elt in enumerate(l):
    print(str(index) + ' + ' + str(elt[2]) + ' - ' + str(index+elt[2]))


for index, elt in enumerate(l):
    pren, nom, an = elt
    print(str(index) + ' + ' + pren + ' - ' + str(index+elt[2]))
