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

#Binary Search using an iterative Quick Sort process for sorting data
def quicksort_and_binary_search(arr, key):
    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for x in range(low, high):
            if a[x] <= pivot:
                i = i + 1
                (a[i], a[x]) = (a[x], a[i])
        (a[i + 1], a[high]) = (a[high], a[i + 1])
        return i + 1

    def quicksort(a, low, high):
        stack = [(low, high)]
        while stack:
            low, high = stack.pop()
            if low < high:
                part = partition(a, low, high)
                stack.append((low, part - 1))
                stack.append((part + 1, high))

    def binary_search(arr, first, last, key):
        while first <= last:
            mid = (first + last) // 2
            if key == arr[mid]:
                return mid
            elif key < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
        return -1  # Key was not found in the array

    quicksort(arr, 0, len(arr) - 1)
    return binary_search(arr, 0, len(arr) - 1, key)

#Function for fitting logrithmic data curve fitting
def func(x, a, b):
    return a * np.log(x) + b

#Shuffles List
def shuffleList (a):
    random.shuffle(a)
    return a

ITERATIONS = 100 #Number of Iterations for timeit

#Inputs from 10, 20, 50, 100, 200, ... to 10 mill, 20 mill, 50 mill
input_sizes = [number * pow(10, i) for i in range(7) for number in [10, 20, 50]] # List comprehension so that it is faster

#Making a list of empty lists of however many input sizes
linearSearchTime = [0] * len(input_sizes)
quickBinaryTime = [0] * len(input_sizes)

#Loops through the element sizes for data
for i, index in enumerate(input_sizes):
    randList = random.sample(range(0, index), index) #A list of random numbers
    targetElement = randList[0] #Target is first element to guarantee the number picked is always in the list
    #Appends total time to linearly search for an element X times for Y input size
    quickTime = 0
    linearTime = 0 
    #Uses for loop instead of number / repeat functions so that it does not time how long it takes to shuffle list
    for x in range(ITERATIONS):
        shuffleList(randList)
        linearTime += timeit.timeit(lambda: linearSearch(randList, index, targetElement), number=1)
        quickTime += timeit.timeit(lambda: quicksort_and_binary_search(randList, targetElement), number=1)
    linearSearchTime[i] = linearTime
    quickBinaryTime[i] = quickTime
        
#Calculating average time for each input size for linear search
avg_linear = [(linearSearchTime[i] / ITERATIONS) for i in range(len(input_sizes))]
avg_quick_binary = [(quickBinaryTime[i] / ITERATIONS) for i in range(len(input_sizes))]

#Linear data curve fitting
slope, intercept = np.polyfit(input_sizes, avg_linear, 1)
plt.scatter(input_sizes, avg_linear, label='Linear Search Avg')
linevalues = [slope * x + intercept for x in input_sizes]
plt.plot(input_sizes, linevalues, 'r')
plt.legend()
plt.savefig("linear_avg.6.4.jpg")
plt.clf() #Clear plot for next plot

#Logrithmic Quick sort binary Search
popt2, pcov2 = scipy.optimize.curve_fit(func, input_sizes, avg_quick_binary)

# Plotting the data and the fitted curve
plt.scatter(input_sizes, avg_quick_binary, label='Quick Sort & Binary Search Avg')

# Plot the fitted curve
x_values2 = np.linspace(min(input_sizes), max(input_sizes), 100)
fitted_curve2 = func(x_values2, *popt2)
plt.plot(x_values2, fitted_curve2, 'r')
plt.legend()
plt.savefig("quick_binary_avg.6.4.jpg")