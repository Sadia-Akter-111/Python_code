def linear_search(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i

    return -1
arr=[1,2,3,4,5,6,7]
print(linear_search(arr,10))


