import timeit
import random 
from matplotlib import pyplot as plt
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

#Shuffles List
def shuffleList (a):
    random.shuffle(a)
    return a

ITERATIONS = 100 #Number of Iterations

#Number of elements for each list
INPUT_SIZE = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

#Making a list of empty lists of however many input sizes
linearSearchTime = []
quickBinaryTime = []

#Loops through the element sizes for data
for index in INPUT_SIZE:
    randList = random.sample(range(0, index), index) #A list of random numbers
    targetElement = randList[0] #Target is first element to guarantee the number picked is always in the list
    quickTime = 0
    linearTime = 0 
    #Uses for loop instead of number / repeat functions so that it does not time how long it takes to shuffle list
    for x in range(ITERATIONS):
        shuffleList(randList)
        linearTime += timeit.timeit(lambda: linearSearch(randList, index, targetElement), number=1)
        quickTime += timeit.timeit(lambda: quicksort_and_binary_search(randList, targetElement), number=1)
    linearSearchTime.append(linearTime)
    quickBinaryTime.append(quickTime)
        
avg_linear = []
avg_quick_binary = []
#Calculating average time for each input size for linear search
for i in range(len(INPUT_SIZE)):
    avg_linear.append(linearSearchTime[i] / ITERATIONS)
    avg_quick_binary.append(quickBinaryTime[i] / ITERATIONS)

#Linear data curve fitting
plt.scatter(INPUT_SIZE, avg_linear, label='Linear Search Avg')
plt.scatter(INPUT_SIZE, avg_quick_binary, label='Quick Sort & Binary Search Avg')
plt.xlabel('Input Sizes')
plt.ylabel('Average Time (s)')
plt.legend()
plt.show()
plt.savefig("LinearVsQuickBinary.6.4.jpg")

#4) Clearly linear search is significantly faster than sorting data first using quick sort
#   and then applying binary search. Searching is always faster than sorting, and therefore,
#   the output is expected. Additionally, linear search is best for when the data is randomized
