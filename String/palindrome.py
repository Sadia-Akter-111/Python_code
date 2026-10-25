s=input("Enter a string: ")
s=s.lower()
l=0
r=len(s)-1
palindrome=True
while l<r:
    if s[l]!=s[r]:
        palindrome=False
        break
    l+=1
    r-=1

if(palindrome):
    print(True)
else:
    print("False")
