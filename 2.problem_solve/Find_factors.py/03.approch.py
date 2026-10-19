#optimal solution
#check 1 to sqrt(n)
from math import sqrt
def factors(n):
    result=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            result.append(i)
            if i!=n//i:
                result.append(n//i)
    return sorted(result)
print(factors(36))