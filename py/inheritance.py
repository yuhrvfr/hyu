# Inheritance
class Animal:
    sound =""
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return("{sound} I am {name}! {sound}".format(
            name=self.name,sound=self.sound))
    def speak(self):
        print(self)
#        print("{sound} I am {name}! {sound}".format(
#            name=self.name,sound=self.sound))

class Piglet(Animal):
    sound = "Oink"

peggy = Piglet('peggy')

peggy.speak()
print(peggy)

class Cow(Animal):
    sound="Mooooo"

berny = Cow('berny')

print(berny)
