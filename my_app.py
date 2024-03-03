#name = input("what is your name? ")
#message = f"Hello {name}"
#print(message)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' is walking')

    def speak(self):
        print(f"My name is {self.name} and my age is {self.age}")



john = Person('John',22)
mariam = Person('Mariam',18)


print(john.name+ ' '+ str(john.age)  )
john.speak()
john.walk()