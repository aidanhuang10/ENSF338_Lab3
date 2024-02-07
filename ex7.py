import sys 
sys.setrecursionlimit(20000)
import timeit
import random 
import numpy as np
from matplotlib import pyplot as plt
import scipy
import json
#Binary Search
def binarySearch (arr, first, last, initial, key):
    if (first <= last):
        mid = initial
        if(key == arr[mid]):
            return mid
        elif(key < arr[mid]):
            return binarySearch(arr, first, mid - 1, (mid // 2), key)
        elif(key > arr[mid]):
            return binarySearch(arr, mid + 1, last, (mid // 2), key)
    return -1 #Key was not found in the array

# def percentiles():
#     numbers = [round(0.1 * i, 1) for i in range(1, 10)]
#     return numbers

# mid_points = percentiles()

#Open and read json file
with open('./ENSF338_Lab3/ex7tasks.json', 'r') as f:
    tasks = json.load(f)

with open('./ENSF338_Lab3/ex7data.json', 'r') as g:
    data = json.load(g)

avg_key_time = []
for target in tasks:
    time = timeit.timeit(lambda: binarySearch(data, 0, len(data) - 1, target, target))
    avg_key_time.append(time)

# avg_time = []
# for target in tasks:
#     time = timeit.timeit(lambda: binarySearch(data, 0, len(data) - 1, (len(data) - 1) // 2))
#     avg_time.append(time)

# plt.scatter(data, avg_time)
# plt.plot()
# plt.scatter(data, avg_key_time)
# plt.show()
    