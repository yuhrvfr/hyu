numbers = [4,6,8,2,9,1,0]
print(sorted(numbers))
print(numbers)

numbers2 = numbers
print(numbers2.sort())
print(numbers2)

names = ['Charles','Herve','Joseph','Alan','Steven','David','Rixin','Richard']
names.sort()
print(names)

names.sort(key=len)
print(names)
