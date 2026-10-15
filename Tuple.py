#A tuple stores multiple values and is written using parentheses()
marks=(95,96,97,95,70,96)
print (marks)
#count:count()
# returns how many times a value occurs
print(marks.count(95))
#index()
# returns the position of the first occurrence
print(marks.index(95))
#Tuple indexing and looping work like lists:
print(marks[0])
for score in marks:
    print(score)