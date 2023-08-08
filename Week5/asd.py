class Cat:
    def __init__(self, name):
        self.name = name

    def say_my_name(self):
        print(self.name)

    def say_dogs_name(self, dog_name):
        print(f"My friend is {dog_name}")


cat1 = Cat(name="Tom")
cat1.say_my_name()
cat1.say_dogs_name("bobas")



class Dog:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def say_my_info(self):
        print(f"My name is {self.name} and my colour is {self.colour}")

    def get_name(self):
        return self.name

dog1 = Dog("bobas", "black")
dog1.say_my_info()
dog_name = dog1.get_name()
print(f"the dog's name is {dog_name}")

# dogs_name = dog1.get_name()
# # cat1.say_dogs_name(dog1.get_name())
# cat1.say_dogs_name(dogs_name)