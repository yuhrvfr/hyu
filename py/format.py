name = 'Joseph'
nb = len(name)*3+2
phrase = 'Your score out of 20 is {score}, good job {person}!'.format(person=name, score=nb)
print(phrase)

price = 7.50
with_tax = price*1.09
print(price,with_tax)
ph ="USD 2 digit only price is ${:.2f} with tax cost is ${:.2f}".format(price,with_tax)
print(ph)

def to_celsius(x):
    return (x-32)*5/9
print()
print("unformatted output of temp conversion:")
for x in range (0,101,10):
    print(str(x) + "F | "+ str(to_celsius(x)) + "C.")
print()
print("Formatted output of temp conversion:")
for x in range (0,101,10):
    print("{tempF:>3} F | {tempC:>6.2f} C.".format(tempF=x,tempC=to_celsius(x)))

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)

formatted_string = "{nom0} {nom2} {nom1}".format(nom2=first, nom1=second, nom0=third)
print(formatted_string)
