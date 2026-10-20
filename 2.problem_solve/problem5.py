nums=[1,7,4,9,8]
largest=nums[0]
for i in range(len(nums)):
    if nums[i]>largest:
        largest=nums[i]

print(largest)