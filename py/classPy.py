class Apple:
    pass

print(Apple)

# help(Apple)

class Apple:
    color = ""
    flavor = ""

# help(Apple)

golden = Apple()

golden.color = 'yellow'
golden.flavor = 'soft'

print(type(golden))

print(golden.flavor)
print(golden.color.upper())

# help(Apple)
# help(golden)

class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
  temp = you.apples
  you.apples = me.apples
  me.apples = temp
  return you.apples, me.apples


class Piglet:
    def speak(self):
        print("oink oink")

hamlet = Piglet()
hamlet.speak()

class Piglet:
    name="piglet"  #default value of name attribute to ensure initialized
    years = 0
    def speak(self):
        print("Oink! I am {}! Oink!".format(self.name.capitalize()))
    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.name = "hamlet"
hamlet.speak()
hamlet.years = 2
print(hamlet.pig_years())

#
# ''' Documentation in help(class) '''
# __init__(self, arg1, ....) constructor with essential arguments
# __str__(self) what to say when stringifying the class used in print( )
#
class Piglet:
    def __init__(self,name,years):
        '''Piget class has 2 attributes name and years'''
        self.name = name
        self.years = years
    def __str__(self):
        '''Return a message with the instance name and age'''
        return('The piglet {name}, {age} years old'.format(name=self.name,age=self.years))
    def speak(self):
        """ Return a message of introduction with the name"""
        print("Oink! I am {}! Oink!".format(self.name.capitalize()))
    def pig_years(self):
        """Convert age of the piglet in piglet years 18X"""
        return self.years * 18


hamlet = Piglet('hamlet',2)
hamlet.speak()
hamlet.years = 2
print(hamlet.pig_years())
print(hamlet)
help(Piglet)
