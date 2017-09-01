def merge(unsortedArray):
    if len(unsortedArray) > 1:
        middle = len(unsortedArray)//2
        left = unsortedArray[:middle]
        right = unsortedArray[middle:]
        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsortedArray[k] = left[i]
                i += 1
            else:
                unsortedArray[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            unsortedArray[k] = left[i]
            i +=1 
            k += 1
        while j < len(right):
            unsortedArray[k] = right[j]
            j += 1
            k += 1


