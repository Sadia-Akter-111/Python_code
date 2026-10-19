#n=5378
#num=n
#while n>0:
#last_digit=n%10
#count+=1
#num//=10
from math import *
def count_digit(num):
    return int(log10(num)+1)

count=count_digit(5738)

print(count)
