#2nd largest element
nums=[55,32,-97,99,3,67]
largest=float("-inf")
s_largets=float("-inf")
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])
for i in range(0,n):
    if nums[i]>s_largets and nums[i]!=largest:
        s_largests=nums[i]

print(s_largests)
print(largest)

