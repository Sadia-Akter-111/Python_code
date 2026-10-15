#A dictionary stores information as key: value pairs
marks={

    "math":95,
    "Eco":90,
    "English":100
}
print(marks)
#Accessing a value
print(marks["Eco"])
#adding new pair
marks["biology"]="99"
print(marks)
#Looping through a dictionary
for subject in marks:
    print(subject, marks[subject])