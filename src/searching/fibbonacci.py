def fibbonacci(num):
    if num < 0:
        print("nah")
        return
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibbonacci(num-1) + fibbonacci(num-2)

def quicksort(arr):
    if len(arr) <=1:
        return arr
    else:
        left=[]
        right=[]
        equal=[]
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                right.append(i)
        return quicksort(left) + equal + quicksort(right)

print(quicksort([4,3,2,1,3,3]))
