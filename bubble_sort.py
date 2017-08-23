def bubble_sort(unsorted_array):
    cached_element = 0
    swapped = False 
    while True:
        for i in range(len(unsorted_array)-1):
            if unsorted_array[i] > unsorted_array[i+1]:
                swapped = True
                cached_element = unsorted_array[i]
                unsorted_array[i] = unsorted_array[i+1]
                unsorted_array[i+1] = cached_element
        if not swapped:
            return unsorted_array
        swapped = False

print (bubble_sort([3,2,7,5,8,1,4,9]))
