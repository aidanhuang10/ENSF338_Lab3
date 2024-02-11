import timeit
import random 
import numpy as np
from matplotlib import pyplot as plt
import scipy
#Traditional Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#Binary Search used for BinaryInsertionSort
def binarySearch(Array, N, key):
    L = 0
    R = N
    while(L < R):
        mid = (L + R)//2
        if (Array[mid] <= key):
            L = mid + 1
        else:
            R = mid - 1
    return L

#BinaryInsertionSort
def binaryInsertionSort(Array):
    # We assume the 1st element of Array to be already sorted.
    # Now we start iterating from the 2nd element to the last element.
    for i in range (1,len(Array)):
        key = Array[i]
        pos = binarySearch(Array, i, key)
        # 'pos' will now contain the index where 'key' should be inserted.
        j = i
        # Shifting every element from 'pos' to 'i' towards right.
        while(j > pos):
            Array[j] = Array[j-1]
            j = j-1
        # Inserting 'key' in its correct position.
        Array[pos] = key

#Function for fitting quadratic data curve fitting
def func(x, a, b):
    return a * np.square(x) + b

SIZE_LIST = [10, 20, 40, 80, 160, 320, 640, 1280] #Sizes for sorting a certain list
RUNS = 100  #Constant number of runs

#Timing for both binary insertion and insertion
binaryInsertion = []
insertion = []

#Testing binary Insertion Sorting algorithm with small but increasing input size
for array in SIZE_LIST:
    #Reseting time it takes for each run with different input sizes
    insertionTime = 0
    binaryInsertionTime = 0
    #Not using RUNS in number because insertion is an in-place sorting algorithm
    #And We do not want to count the time it takes to randomize a list
    for iterations in range(RUNS):
        #Copy of list to ensure both algorithms uses same lists for testing
        randList = random.sample(range(0, array), array)
        copyOfRandList = randList.copy()
        insertionTime += timeit.timeit(lambda: insertionSort(randList), number=1)
        binaryInsertionTime += timeit.timeit(lambda: binaryInsertionSort(copyOfRandList), number=1)
    binaryInsertion.append(binaryInsertionTime)
    insertion.append(insertionTime)

avg_binary_insertion = []
avg_insertion_list = []
#Calculating average time for each input size for binary insertion sort & regular insertion sort 
for i in range(len(SIZE_LIST)):
    avg_binary_insertion.append(binaryInsertion[i] / RUNS)
    avg_insertion_list.append(insertion[i] / RUNS)

popt, pcov = scipy.optimize.curve_fit(func, SIZE_LIST, avg_insertion_list)
popt2, pcov2 = scipy.optimize.curve_fit(func, SIZE_LIST, avg_binary_insertion)

# Plotting the data and the fitted curve
plt.scatter(SIZE_LIST, avg_insertion_list, label='Insertion Sort')
plt.scatter(SIZE_LIST, avg_binary_insertion, label='Binary Insertion Sort')

# Plot the fitted curve
x_values = np.linspace(min(SIZE_LIST), max(SIZE_LIST), 100)
fitted_curve = func(x_values, *popt)
fitted_curve2 = func(x_values, *popt2)

plt.plot(x_values, fitted_curve, 'b')
plt.plot(x_values, fitted_curve2, 'r')
plt.xlabel('Input Sizes')
plt.ylabel('Average Time (s)')
plt.legend()
plt.savefig("InsertionVsBinaryInsertion.5.3.jpg")

#4) On average, both algorithms are essentially the same speed. However, binary insertion sort is faster by a bit
#   due to the fact that binary insertion sort uses fewer comparisons than traditional insertion sort does.