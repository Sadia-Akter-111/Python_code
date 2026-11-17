class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Breed:", self.breed)


d = Dog("Cherry", 5, "Indian")

d.display()