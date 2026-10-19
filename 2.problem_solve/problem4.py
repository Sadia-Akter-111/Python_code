n=1634
nod=len(str(n))
total=0
num=n

while num>0:
    rem=num%10
    total=total+rem**nod
    num//=10

if total==n:
    print(True)
else:
    print(False)