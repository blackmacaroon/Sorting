# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrayA, arrayB ):
    elements = len( arrayA ) + len( arrayB )
    merged_array = [0] * elements       #what is this doing?
    a = 0    #current indexes for arrays
    b = 0
    for i in range(elements):
        #find the smallest first-item in the arrays
        # add that to "elements" at the given index
        # increment the a & b counter
        if a >= len(arrayA):
            # 1. A is empty, B is not empty
            merged_array[i] = arrayB[b]
            b += 1
        elif b >= len(arrayB):
            # 2. B is empty, A is not empty
            merged_array[i] = arrayA[a]
            a += 1
        elif arrayA[a] < arrayB[b]:
            # 3. A has the smaller element
            merged_array[i] = arrayA[a]
            a += 1
        else: # arrayA[a_i] >= arrayB[b_i]:
            # 4. B has the smaller element
            merged_array[i] = arrayB[b]
            b += 1
    
    return merged_array
    
    # # TO-DO
    # #loop through each array, hold the value in memory - so I can compare the first index (that we know is the lowest #) in each array i, j = 0, 0
    # i = 0 
    # j = 0
    # k = 0
    # # as long as each index is within the range of their array's length
    # # while i in range (0, len(arrayA) -1) or j in range (0, len(arrayB) -1):
    # # aka:
    # while i < len(arrayA) and j < len(arrayB):
    #     #check if the first element in the first array is smaller than the first element in the second array
    #     if arrayA[i] < arrayB[j]:
    #         #if yes, store first element from first array in merged_array, increase index by 1 for next search 
    #         merged_array = arrayA[i]
    #         i = i + 1
    #         k = k + 1
    #     else:
    #         merged_array = arrayB[j]
    #         j = j + 1
    #         k = k + 1
    # while i < len(arrayA):
    #     merged_array[k] = arrayA[i]
    #     k = k + 1
    #     i = i + 1
    # while k < len(arrayB):
    #     merged_array[k] = arrayB[j]
    #     k = k + 1
    #     j = j + 1
    # print("array after merging")
    # for i in range(len(arrayA) + len(arrayB)):
    #     print(str(merged_array[i], end = " "))

    # return merged_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( array ):
    # TO-DO
    # base case, when do we want it to stop? when the array has no more numbers? on it's last number? len(arr)<=0 or is it <=1??
    # while your data set contains more than one item, split it in half
    if len(array) > 1:
        # split until the arrays lengths all = 1
        midway_point = len(array) // 2
        left_array = array[ : midway_point]
        right_array = array[midway_point : ]
        #sort the split arrays
        sorted_left = merge_sort(left_array)
        sorted_right = merge_sort(right_array)
        # merge th sorted arrays
        array = merge(sorted_left, sorted_right) 
    return array    



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(array, start, mid, end):
    # TO-DO

    return array

def merge_sort_in_place(array, l, r): 
    # TO-DO

    return array


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/arraysort.txt
def timsort( array ):

    return array
