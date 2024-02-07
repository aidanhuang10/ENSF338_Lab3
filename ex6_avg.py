import sys 
sys.setrecursionlimit(20000)
import timeit
import random 
import numpy as np
from matplotlib import pyplot as plt
import scipy
#Linear Search 
def linearSearch (arr, n, key):
    for i in range(n):
        if key == arr[i]:
            return i
    return -1 #Key was not found in array

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
        quickSort(a, part + 1, high)

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

#Generating a list of size X
def listGeneratorOfSize(size):
    vector = random.sample(range(0, 50000000), size)
    return vector

#Creates empty list for calculating average time of X number(s) of inputs
def emptyListCreator(num):
    vector = []
    for x in range(num):
        vector.append([])
    return vector

#Function for fitting quadratic data curve fitting
def func(x, a, b):
    return a * np.log(x) + b

#Inputs from 10, 20, 50, 100, 200, ... to 10 mill, 20 mill, 50 mill
input_sizes = []
for i in range(7):
    for number in [10, 20, 50]:
        input_sizes.append(number * pow(10, i))

#Making a list of empty lists of however many input sizes
linearSearchTime = emptyListCreator(len(input_sizes))
quickBinaryTime = emptyListCreator(len(input_sizes))

# for index in input_sizes:
#     randList = listGeneratorOfSize(index)
#     targetElement = randList[0]
#     for array in linearSearchTime:
#         for i in range(1000):
#             random.shuffle(randList)
#             linearTime = timeit.timeit(lambda: linearSearch(randList, index, targetElement))
#             array.append(linearTime)
        
# #Calculating average time for each input size for linear search
# avg_linear = []
# for i in range(len(input_sizes)):
#     avg_linear.append(sum(linearSearchTime[i]) / len(linearSearchTime[i]))

#Quick sort and Binary Search
for index in input_sizes:
    randList = listGeneratorOfSize(index)
    targetElement = randList[0]
    for array in quickBinaryTime:
        for i in range(1000):
            quickTime = timeit.timeit(lambda: quickSort(randList, 0, len(randList) - 1))
            binaryTime = timeit.timeit(lambda: binarySearch(randList, 0, len(randList), targetElement))
            array.append(quickTime + binaryTime)

avg_quick_binary = []
for i in range(len(input_sizes)):
    avg_quick_binary.append(sum(quickBinaryTime[i]) / len(quickBinaryTime[i]))

# #Linear data curve fitting
# slope, intercept = np.polyfit(input_sizes, avg_linear, 1)
# plt.scatter(input_sizes, avg_linear)
# linevalues = [slope * x + intercept for x in input_sizes]
# plt.plot(input_sizes, linevalues, 'r')
# plt.savefig("./ENSF338_Lab3/linear.6.4.jpg")
# plt.clf()

#Logrihtmic Quick sort and binary Search
popt2, pcov2 = scipy.optimize.curve_fit(func, input_sizes, avg_quick_binary)

# Plotting the data and the fitted curve
plt.scatter(input_sizes, avg_quick_binary, label='Binary Insertion Sort')

# Plot the fitted curve
x_values2 = np.linspace(min(input_sizes), max(input_sizes), 100)
fitted_curve2 = func(x_values2, *popt2)
plt.plot(x_values2, fitted_curve2, 'r')
plt.legend()
plt.savefig("quick_binary.6.4.jpg")