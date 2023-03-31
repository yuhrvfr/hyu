sentence = "This is a list so it is mutable."
print(sentence)
list = sentence.split()
print(list)
len(list)
list[0]
list.append("Unlike strings are not mutable.".split())

print(list)
for i in range(len(list)):
    print(list[i])


list2 = "This is a list so it is mutable.".split()
list3 = "Unlike strings are not mutable.".split()
list2.extend(list3)

print(list2)

fruits = ["Apple", "Banana", "Orange"]
fruits.append("Kiwi")
print(fruits)
fruits.insert(0,"Clementine")
print(fruits)

fruits.remove("Banana")
print(fruits)

print('2: '+fruits.pop(2))
#fruits.pop(2)
print(fruits)

fruits[1] = "Durion"
print(fruits)
