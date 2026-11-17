class Student :
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self)->None:
        print("My name is: ",self.name)
        print("Age is: ",self.age)
        print("Gender: ",self.gender)
s1=Student("sadia",21,"Female")
s1.display()

