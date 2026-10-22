def LB(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans
arr=[1,1,1,1,2,2,2,3,3,4,5,6,7]
print(LB(arr,2))