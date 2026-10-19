n=1221
result=0
num=n

while num>0:
    rem=num%10
    result=result*10+rem
    num//=10

if result==n:
    print(True)
else:
    print(False)