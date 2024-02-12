"""
1. Implement a basic version of that function, using the code seen in
class for the rest of the algorithm [0.2 pts]
"""
import sys
sys.setrecursionlimit(20000)

arr = [8, 42, 25, 3, 3, 2, 27, 3]
def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


#combine two sub arrays that are sorted 
def merge(arr, low, mid, high):

    sub_array1 = arr[low:mid + 1]
    sub_array2 = arr[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    while (i < len(sub_array1)) and (j < len(sub_array2)):
        if sub_array1[i] <= sub_array2[j]:
            arr[k] = sub_array1[i]
            i += 1
        else:
            arr[k] = sub_array2[j]
            j += 1
        k += 1

    while (i < len(sub_array1)):
        arr[k] = sub_array1[i]
        i += 1
        k += 1

    while (j < len(sub_array2)):
        arr[k] = sub_array2[j]
        j += 1
        k += 1

merge_sort(arr, 0, len(arr) - 1)
print(arr)


