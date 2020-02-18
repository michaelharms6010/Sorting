# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    indexa = 0
    indexb = 0
    for i in range(0, elements):
        if indexa >= len(arrA):
            merged_arr[i] = arrB[indexb]
            indexb += 1
        elif indexb >= len(arrB):
            merged_arr[i] = arrA[indexa]
            indexa += 1
        elif arrA[indexa] < arrB[indexb]:
            merged_arr[i] = arrA[indexa]
            indexa += 1
        else:
            merged_arr[i] = arrB[indexb]
            indexb += 1
    return merged_arr

print(merge([1,2], [3,4]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr
    else:
        left=arr[: len(arr) // 2 ]
        right=arr[len(arr) // 2 :]
        return merge(merge_sort(left), merge_sort(right))

print(merge_sort([3,2,1,4]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    left = arr[start:mid]
    right = arr[mid:end]
    lefti = 0
    righti = 0
    for i in range(start, end):
        if righti >= len(right) or (lefti < len(left) and left[lefti] < right[righti]):
            arr[i] = left[lefti]
            lefti += 1
        else:
            arr[i] = right[righti]
            righti += 1

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if r-l > 1:
        middle = (l + r) // 2
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle, r)
        merge_in_place(arr, l, middle, r)

    return arr

print(merge_sort_in_place([23,15,3,1,5], 0, 5))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
