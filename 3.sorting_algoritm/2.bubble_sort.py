def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swaps=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps=True
        if not swaps:
            break
              
        
    return arr
arr=[5,1,9,6,8,2,3]
print("sorting array: ",bubble_sort(arr))


                