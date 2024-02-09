import timeit
from matplotlib import pyplot as plt
import json

#Selected Midpoint Binary Search
def selectedMidPointBinarySearch (arr, first, last, selected_mid, key):
    if (first <= last):
        mid = selected_mid
        if(key == arr[mid]):
            return mid
        elif(key < arr[mid]):
            return selectedMidPointBinarySearch(arr, first, mid - 1, (first + mid - 1) // 2, key)
        elif(key > arr[mid]):
            return selectedMidPointBinarySearch(arr, mid + 1, last, (mid + 1 + last) // 2, key)
    return -1 #Key was not found in the array

#Regular Binary Search
def BinarySearch (arr, first, last, key):
    if (first <= last):
        mid = (first + last) // 2
        if(key == arr[mid]):
            return mid
        elif(key < arr[mid]):
            return BinarySearch(arr, first, mid - 1, key)
        elif(key > arr[mid]):
            return BinarySearch(arr, mid + 1, last, key)
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

avg_selected_time = []
avg_regular_time = []
for target in tasks:
    #Uses the key as the mid point of division  
    selectedMiddleTime = timeit.timeit(lambda: selectedMidPointBinarySearch(data, 0, len(data) - 1, target, target), number=1)
    regularTime = timeit.timeit(lambda: BinarySearch(data, 0, len(data) - 1, target), number=1)
    avg_selected_time.append(selectedMiddleTime)
    avg_regular_time.append(regularTime)
    
# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(tasks, avg_selected_time, label='Selected Middle Binary Search', marker='o', color='blue')
plt.scatter(tasks, avg_regular_time, label='Regular Binary Search', marker='o', color='red')
plt.xlabel('Target Value')
plt.ylabel('Average Time (s)')
plt.title('Average Search Time for Each Target using Binary Search Regular VS Selected Mid Point')
plt.grid(True)
plt.legend()
plt.show()

    