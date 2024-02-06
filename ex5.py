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

#Testing each sorting algorithm with small but increasing sample size
vector1 = random.sample(range(0, 10000), 100)
vector2 = random.sample(range(0, 10000), 200)
vector3 = random.sample(range(0, 10000), 400)
vector4 = random.sample(range(0, 10000), 800)
vector5 = random.sample(range(0, 10000), 1600)
vector6 = random.sample(range(0, 10000), 3200)

attempt_list = [100, 200, 400, 800, 1600, 3200]

time_vector1_list = []
time_vector2_list = []
time_vector3_list = []
time_vector4_list = []
time_vector5_list = []
time_vector6_list = []

for i in range(1000):
    time_vector1 = timeit.timeit(lambda: binaryInsertionSort(vector1), number=100)
    time_vector1_list.append(time_vector1)
    time_vector2 = timeit.timeit(lambda: binaryInsertionSort(vector2), number=100)
    time_vector2_list.append(time_vector2)
    time_vector3 = timeit.timeit(lambda: binaryInsertionSort(vector3), number=100)
    time_vector3_list.append(time_vector3)
    time_vector4 = timeit.timeit(lambda: binaryInsertionSort(vector4), number=100)
    time_vector4_list.append(time_vector4)
    time_vector5 = timeit.timeit(lambda: binaryInsertionSort(vector5), number=100)
    time_vector5_list.append(time_vector5)
    time_vector6 = timeit.timeit(lambda: binaryInsertionSort(vector6), number=100)
    time_vector6_list.append(time_vector6)

avg_binary_insertion = []
avg_binary_insertion.append(sum(time_vector1_list) / len(time_vector1_list))
avg_binary_insertion.append(sum(time_vector2_list) / len(time_vector2_list))
avg_binary_insertion.append(sum(time_vector3_list) / len(time_vector3_list))
avg_binary_insertion.append(sum(time_vector4_list) / len(time_vector4_list))
avg_binary_insertion.append(sum(time_vector5_list) / len(time_vector5_list))
avg_binary_insertion.append(sum(time_vector6_list) / len(time_vector6_list))  


time_vector1_list = []
time_vector2_list = []
time_vector3_list = []
time_vector4_list = []
time_vector5_list = []
time_vector6_list = []

for i in range(1000):
    time_vector1 = timeit.timeit(lambda: insertionSort(vector1), number=100)
    time_vector1_list.append(time_vector1)
    time_vector2 = timeit.timeit(lambda: insertionSort(vector2), number=100)
    time_vector2_list.append(time_vector2)
    time_vector3 = timeit.timeit(lambda: insertionSort(vector3), number=100)
    time_vector3_list.append(time_vector3)
    time_vector4 = timeit.timeit(lambda: insertionSort(vector4), number=100)
    time_vector4_list.append(time_vector4)
    time_vector5 = timeit.timeit(lambda: insertionSort(vector5), number=100)
    time_vector5_list.append(time_vector5)
    time_vector6 = timeit.timeit(lambda: insertionSort(vector6), number=100)
    time_vector6_list.append(time_vector6)

avg_insertion_list = []
avg_insertion_list.append(sum(time_vector1_list) / len(time_vector1_list))
avg_insertion_list.append(sum(time_vector2_list) / len(time_vector2_list))
avg_insertion_list.append(sum(time_vector3_list) / len(time_vector3_list))
avg_insertion_list.append(sum(time_vector4_list) / len(time_vector4_list))
avg_insertion_list.append(sum(time_vector5_list) / len(time_vector5_list))
avg_insertion_list.append(sum(time_vector6_list) / len(time_vector6_list))

# 3)

# Linear data curve fitting
slope, intercept = np.polyfit(attempt_list, avg_insertion_list, 1)
plt.scatter(attempt_list, avg_insertion_list)
linevalues = [slope * x + intercept for x in attempt_list]
plt.plot(attempt_list, linevalues, 'r')
plt.savefig("insertion.5.3.jpg")
plt.clf()

#Function for fitting logarithmic data curve fitting
def func(x, a, b):
    return a * np.square(x) + b

popt, pcov = scipy.optimize.curve_fit(func, attempt_list, avg_binary_insertion)

# Plotting the data and the fitted curve
plt.scatter(attempt_list, avg_binary_insertion, label='Binary Insertion Sort')

# Plot the fitted curve
x_values = np.linspace(min(attempt_list), max(attempt_list), 100)
fitted_curve = func(x_values, *popt)
plt.plot(x_values, fitted_curve, 'r-')
plt.legend()
plt.savefig("binaryInsertion.5.3.jpg")

#4) 