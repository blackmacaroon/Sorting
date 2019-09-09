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
        #if the next is larger, variables shift and the next index starts the next round as the temp
        # this is swapping, temp becomes smallest, smallest becomes current and current becomes temp
        ## temp = arr[smallest_index]
        ## arr[smallest_index] = arr[cur_index]
        ## arr[cur_index] = temp       #aka:
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr




# TO-DO:  implement the Bubble Sort function below
#compare 1st pair of elements
    #if the RHS is less than the LHS, swap
    #else do nothing
# iterate through the array, comparing other pairs of adjacent elements
# if one or more swaps performed, repeat the above process

def bubble_sort( arr ):
    #if there was no swap, we're done!, else..
    swap_occured = True
    while swap_occured:
        #switch swap to false, assuming each time is the last
        swap_occured = False
        # loop through first number...
        for i in range(0, len(arr)):
            # and second...
            for j in range(0, len(arr)):
                # compare
                if(arr[i] < arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
                    # if a swap occured, switch back to true to revalidate the loop
                    swap_occured = True

        return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr