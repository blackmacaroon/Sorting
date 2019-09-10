# TO-DO: complete the helper function below to merge 2 sorted lists
def merge( listA, listB ):
    elements = len( listA ) + len( listB )
    merged_list = [0] * elements
    # TO-DO
    #loop through each list, compare the first index (that we know is the lowest #) in each list i, j = 0, 0
    i, j, k = 0, 0, 0
    # as long as each index is within the range of their list's length
    # while i in range (0, len(listA) -1) or j in range (0, len(listB) -1):
    # aka:
    while i < len(listA) and j < len(listB):
        #check if the first element in the first list is smaller than the first element in the second list
        if listA[i] < listB[j]:
            #if yes, store first element from first list in merged_list, increase index by 1 for next search 
            merged_list = listA[i]
            i = i + 1
            k = k + 1
        else:
            merged_list = listB[j]
            j = j + 1
            k = k + 1


    
    return merged_list


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( list ):
    # TO-DO

    return list


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(list, start, mid, end):
    # TO-DO

    return list

def merge_sort_in_place(list, l, r): 
    # TO-DO

    return list


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( list ):

    return list
