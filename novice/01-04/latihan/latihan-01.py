# Inheritance Revisited
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):
    def speak(self):
        return self.name+' says Meow!'
    

class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        self.name = name
        self.legs = legs
        self.hibernate = hibernate
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())


yogi = Bear('Yogi')
print(yogi.name)
print(yogi.legs)
print(yogi.hibernate)