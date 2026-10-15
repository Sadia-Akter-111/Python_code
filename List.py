#List 
marks=[95,96,97,'A',100]
print(marks)
print(len(marks))
#indexing
print(marks[0])
print (marks[1])
#slicing
print(marks[0:3])
#Looping through a list
for score in marks:
    print(score)
    #ADD element
    marks.append
    print(marks)

#insert
marks.insert(0,100)
print(marks)
#checking for element
print(10 in marks)#false
print(100 in marks)#true
#clearing a list
marks.clear()
print(marks)
print(len(marks))