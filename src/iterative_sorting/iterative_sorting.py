# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements - through the indexes, not the values, starting with position zero, "what should be here"
    # loop all the way through each index until you get to the second-to-last...
    for i in range(0, len(arr) - 1):   # looping through all the values in the dataset
        cur_index = i
        # to find and assign the smallest
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # check everything to the right of the first index
        for j in range(cur_index, len(arr)):   #looping through everything to the right of our new array we want to fill
        # j is the new array, starting with your i value
        # if the new array number is less than the next, nothing changes  
            if arr[j] < arr[smallest_index]:
                smallest_index = j 
        # TO-DO: swap
        #if the next is larger
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
#compare 1st pair of elements
    #if the RHS is less than the LHS, swap
    #else do nothing
# iterate through the array, comparing other pairs of adjacent elements
# if one or more swaps performed, repeat the above process

def bubble_sort( arr ):
    # swap_occured = True
    # while swap_occured:
    #     swap_occured = False
    #     for i in range(0, len(arr)-2):
    #         if i > i+1:
    #             smallest_index = i
    #             # restart the loop with the next pair - "revalidate swap_occured"
    #             swap_occured = True 


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr