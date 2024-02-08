import sys 
sys.setrecursionlimit(20000000)
import random
import timeit
import numpy as np
from matplotlib import pyplot as plt
import scipy

#Partition Method for Quicksort
def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for x in range(low, high):
        if a[x] <= pivot:
            i = i + 1
            (a[i], a[x]) = (a[x], a[i])
    (a[i + 1], a[high]) = (a[high], a[i + 1])
    return i + 1

#Quick Sort
def quickSort(a, low, high):
    if low < high:
        part = partition(a, low, high)
        quickSort(a, low, part - 1)
        quickSort(a, part, high)

#Binary Search
def binarySearch (arr, first, last, key):
    if (first <= last):
        mid = (first + last) // 2
        if(key == arr[mid]):
            return mid
        elif(key < arr[mid]):
            return binarySearch(arr, first, mid - 1, key)
        elif(key > arr[mid]):
            return binarySearch(arr, mid + 1, last, key)
    return -1 #Key was not found in the array

#Function for fitting quadratic data curve fitting
def func(x, a, b):
    return a * np.square(x) + b

#Shuffles List
def shuffleList (a):
    random.shuffle(a)
    return a

# Generates Inputs from 10, 20, 50, 100, 200, ... to 10 mill, 20 mill, 50 mill       
input_sizes = [number * pow(10, i) for i in range(7) for number in [10, 20, 50]] # List comprehension so that it is faster
quickBinaryTime = [0 for x in range(len(input_sizes))]

#Quick sort and Binary Search
for i, index in enumerate(input_sizes):
    randList = [random.randint(0,index + 1) for x in range(index)] #A list of random numbers
    targetElement = randList[0] #Target is first index (guarantees the element being searched for is always the same)
    quickTime = timeit.timeit(lambda: quickSort(shuffleList(randList), 0, len(randList) - 1), number=50)
    binaryTime = timeit.timeit(lambda: binarySearch(randList, 0, len(randList), targetElement), number=50)
    quickBinaryTime[i] = quickTime + binaryTime
    print("Iteration for QUICK BINARY RECURSIVE#", i, "Done For INPUT_SIZE:", index)
    # print(quickBinaryTime, end='\n')

#Average Time of execution for specified size of input
avg_quick_binary = [sum(quickBinaryTime[i]) / 1000 for i in range(len(input_sizes))]

#Logrihtmic Quick sort and binary Search
popt2, pcov2 = scipy.optimize.curve_fit(func, input_sizes, avg_quick_binary)

# Plotting the data and the fitted curve
plt.scatter(input_sizes, avg_quick_binary, label='Worst Case Quick Sort & Binary Search')

# Plot the fitted curve
x_values2 = np.linspace(min(input_sizes), max(input_sizes), 100)
fitted_curve2 = func(x_values2, *popt2)
plt.plot(x_values2, fitted_curve2, 'r')
plt.legend()
plt.savefig("worst_case_quick_binary.6.4.jpg")