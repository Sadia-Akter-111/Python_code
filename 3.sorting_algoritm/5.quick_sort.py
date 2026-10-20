def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while i<=high and arr[i]<=pivot:
            i+=1
        while j>low and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]

    arr[low],arr[j]=arr[j],arr[low]
    return j
def quick_sort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
    return arr
arr=[4,7,1,6,3,2,8]
print("sorted array: ",quick_sort(arr,0,len(arr)-1))

           
