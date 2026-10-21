def removeDuplicates(arr):
        # Edge case: if the array has only 1 element, it's already unique
        if len(arr) <= 1:
            return len(arr)
        
        i = 0
        j = 1
        
        while j < len(arr):
            # If we find a new unique element
            if arr[j] != arr[i]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            j += 1
            
        # Return the count of unique elements (index + 1)
        return i + 1
arr=[1,1,1,1,1,2,2,4,4,5,6,4,7,8]
print(removeDuplicates(arr))
    