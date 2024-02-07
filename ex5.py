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
            R = mid
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

#Generating a list of size X with random numbers in each element
def listGeneratorOfSize(size):
    vector = random.sample(range(0, 10000), size)
    return vector

#Creates empty list for calculating average time of X number(s) of inputs
def emptyListCreator(num):
    vector = []
    for x in range(num):
        vector.append([])
    return vector

#Function for fitting quadratic data curve fitting
def func(x, a, b):
    return a * np.square(x) + b

SIZE_LIST = [10, 20, 40, 80, 160, 320] #Sizes for sorting a certain list
RUNS = 100  #Constant number of runs for lambda function

#Making a list of empty lists of however many input sizes
time_vectors = emptyListCreator(len(SIZE_LIST))

#Testing binary Insertion Sorting algorithm with small but increasing input size
for i in range(100):
    index = 0
    for array in time_vectors:
        time = timeit.timeit(lambda: binaryInsertionSort(listGeneratorOfSize(SIZE_LIST[index])), number=RUNS)
        array.append(time)
        index += 1

#Calculating average time for each input size for binary insertion sort
avg_binary_insertion = []
for i in range(len(SIZE_LIST)):
    avg_binary_insertion.append(sum(time_vectors[i]) / len(time_vectors[i]))

#Empty the list to use it for Insertion now
time_vectors = emptyListCreator(len(SIZE_LIST))

#Testing Insertion Sorting algorithm with small but increasing input size
for i in range(100):
    index = 0
    for array in time_vectors:
        time = timeit.timeit(lambda: insertionSort(listGeneratorOfSize(SIZE_LIST[index])), number=RUNS)
        array.append(time)
        index += 1

#Calculating average time for each input size for insertion sort
avg_insertion_list = []
for i in range(len(SIZE_LIST)):
    avg_insertion_list.append(sum(time_vectors[i]) / len(time_vectors[i]))

popt, pcov = scipy.optimize.curve_fit(func, SIZE_LIST, avg_insertion_list)

# Plotting the data and the fitted curve
plt.scatter(SIZE_LIST, avg_insertion_list, label='Insertion Sort')

# Plot the fitted curve
x_values = np.linspace(min(SIZE_LIST), max(SIZE_LIST), 100)
fitted_curve = func(x_values, *popt)
plt.plot(x_values, fitted_curve, 'b')

popt2, pcov2 = scipy.optimize.curve_fit(func, SIZE_LIST, avg_binary_insertion)

# Plotting the data and the fitted curve
plt.scatter(SIZE_LIST, avg_binary_insertion, label='Binary Insertion Sort')

# Plot the fitted curve
x_values2 = np.linspace(min(SIZE_LIST), max(SIZE_LIST), 100)
fitted_curve2 = func(x_values2, *popt2)
plt.plot(x_values2, fitted_curve2, 'r')
plt.legend()
plt.savefig("Insertion.vs.BinaryInsertion.5.3.jpg")

#4) On average, both algorithms are essentially the same speed. However, binary insertion sort is faster by a bit
#   due to the fact that binary insertion sort uses fewer comparisons than traditional insertion sort does.