def bubble_sort(unsorted_array):
    cached_element = 0
    swapped = False 
    # TODO: Get rid of this loop and make sure that you are not looping through the whole array
    # every time you try to sort element as the elements towards the end are already greatests 
    # and sorted.
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

