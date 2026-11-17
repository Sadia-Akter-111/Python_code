def Max_sub_sum(nums):
    n=len(nums)
    maxi=float("-inf")
    curSum=0
    for num in nums:
        curSum+=num
        maxi=max(maxi,curSum)
        if curSum<0:
            curSum=0
    return maxi
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(Max_sub_sum(nums))