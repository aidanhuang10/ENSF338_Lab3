import timeit
from matplotlib import pyplot as plt

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

ITERATIONS = 100 #Number of Iterations

#Inputs from 10, 20, 50, 100, 200, ... to 10 mill, 20 mill, 50 mill
INPUT_SIZE = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

quickBinaryTime = []
#Loops through the element sizes for data
for i, index in enumerate(INPUT_SIZE):
    #A list of same elements to test worst case for Quick Sort..
    #When list is sorted ascending and pivot is the biggest element
    randList = [x for x in range(index)]
    targetElement = randList[0] #Target is first element to guarantee the number picked is always in the list
    print(randList)
    quickTime = timeit.timeit(lambda: quicksort_and_binary_search(randList, targetElement), number=ITERATIONS)
    print(randList)
    quickBinaryTime.append(quickTime)
        
#Calculating average time for each input size for quick sort binary search
avg_quick_binary = [(quickBinaryTime[i] / ITERATIONS) for i in range(len(INPUT_SIZE))]

plt.scatter(INPUT_SIZE, avg_quick_binary, label='Worst Case Quick Sort & Binary Search')
plt.xlabel('Input Sizes')
plt.ylabel('Average Time (s)')
plt.legend()
plt.savefig("WorstQuickBinary.6.5.jpg")

#5) As discussed before, since linear search is already faster than sorting the data first and then searching for it,
#   linear search would be faster than this; especially when you are incurring the worst-case performance for 
#   quick sort. Additionally, since the target is the first element of the list, it is also the worst case for 
#   binary search as well.