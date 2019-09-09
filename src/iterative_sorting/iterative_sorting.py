# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements - through the indexes, not the values, position zero, "what should be here"
    # loop all the way through each index until you get to the second-to-last
    for i in range(0, len(arr) - 1):
        cur_index = i
        #to find and assign the smallest
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # check everything to the right of the first index
        for j in range(cur_index, len(arr)):
        # j is the new array, starting with your i value
        #if the new array number is less than the next, nothing changes  
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc) 
             
        # TO-DO: swap
        #if the next is larger
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_occured = true
    while swap_occured:
        for i in range(0, len(arr)-2):
            cur_index = i
            smallest_index = cur_index
            if i > i+1
                smallest_index = i

        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr