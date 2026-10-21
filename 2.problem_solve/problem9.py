#right roated array by k places
def roated(arr,k):
    n=len(arr)
    r=(k%n)
    arr[:]=arr[n-r:n]+arr[0:n-r]

    return arr
arr=[1,2,3,4,5,6,7]
print(roated(arr,3))