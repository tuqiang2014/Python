## Animal is-a object (yes,sort of confusing ) look at the extra credit 
class Animal(object):

	pass
## is-a
class Dog(Animal):

	def _int_(self, name):
		# has-a
		self.name = name

# is-a
class Cat(Animal):

	def _int_(self, name):
		#has-a
		self.name = name
		
#is-a
class Person(object):

	def _int_(self, name):
		# has-a
		self.name = name

#Person has-a pet of some kinf
		self.pet = None
		
# is-a 
class Employee(Person):
	def _int_(self, name, salary):
		
		super(Employee, self)._int_(name)
		
		self.salary = salary


# is-a
class Fish(object):
	pass

# is-a
class Salmon(Fish):
	pass


class Halibut(Fish):
	pass



rover = Dog("Rover")


satan = Cat("Satan")


matty = Person("Marry")


marry.pet = satan


frank = Employee("Frank", 120000)


frank.pet = rover

flipper = Fish()



crouse = Salmon()


harry = Halibut()