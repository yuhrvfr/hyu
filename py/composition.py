class Repository:
      def __init__(self):
          self.packages = {}
      def add_package(self, package):
          self.packages[package.name] = package
      def total_size(self):
          result = 0
          for package in self.packages.values():
              result += package.size
          return result
      def get_package_list(self):
          return self.packages



class Package:
    def __init__(self,name,publisher,size):
        self.name = name
        self.publisher = publisher
        self.size = size
    def __str__(self):
        return(self.publisher + ' ' + self.name + ' '+ str(self.size))


db = Package('database','oracle',1000)
office = Package('office','microsoft',100)
antivirus = Package('defender','norton',80)

office_desktop = Repository()
office_desktop.add_package(office)
office_desktop.add_package(antivirus)

data_server = Repository()
data_server.add_package(db)
data_server.add_package(antivirus)

rep = {}

rep['office'] = office_desktop
rep['server'] = data_server

for val in rep.values():
    for key,value in val.get_package_list().items():
         print(key, end=' : ')
         #for i in range(len(value)):
         print(value)
    print(val.total_size())

#----------------------------


class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def __str__(self):
      text =''
      print(len(self.stock['name']))
      for i in range(len(self.stock['name'])):
          text += self.stock['name'][i] + ' ' + self.stock['material'][i] + ' ' +str(self.stock['amount'][i])+'\n'
      return (text)
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock.get('material'):
      #print(item)
      if item == material:
        #print('ici ' + str(Clothing.stock['amount'][n]))
        count += Clothing.stock['amount'][n]
        n+=1
    return count




class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"

polo = shirt("Polo")

#print(polo)


sweatpants = pants("Sweatpants")

polo.add_item(polo.name, polo.material, 4)
print(polo)

sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
print(sweatpants)


current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


#--------------------
swimsuit = Clothing('swimsuit')
# help(swimsuit)
swimsuit.stock['name'] = ['jamber','unibody','bikini']
swimsuit.stock['material'] = ['polyester','teflon','spandex']
swimsuit.stock['amount'] = [10, 3, 1]

print(swimsuit)
print(swimsuit.stock)




#-----------------------

class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


class Turtle(Animal):
    category ="reptile"

print(Turtle.category)


class Snake(Animal):
    category = "reptile"


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category
