import timeit
import random
from matplotlib import pyplot as plt
def bubbleSort(a,len):
    for y in range(len-1):
        swaps = False
        for x in range (len-1-y):
            if a[x] > a[x+1]:
                swaps = True
                (a[x],a[x+1]) = (a[x+1],a[x])
        if swaps == True:
            break
def partition(a, low, high):
    pivot = a[low]
    left = low+1
    right = high
    done = False
    while not done:
        while left <= right and a[left] <= pivot:
            left = left +1
        while a[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            a[left],a[right] = a[right],a[left]
    a[low],a[right] = a[right],a[low]
    return right
def quickSort(a,low,high):
    if low < high:
        pivot = partition(a,low,high)
        quickSort(a,low,pivot)
        quickSort(a,pivot+1,high)
#sizes of choice: 2,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50,75,100,125,150
bestBubble = []
worstBubble = []
averageBubble = []
worstQuick = []
averageQuick = []
choices = [2,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50,75,100,125,150]
for x in range(20):
    test1 = [y for y in range(choices[x])]#bubble best
    bestBubble.append(timeit.timeit(lambda: bubbleSort(test1,len(test1)), number=1))
    test1 = [choices[x] - y for y in range(choices[x])]#bubble worse case
    test2 = [choices[x] - y for y in range(choices[x])]#quick worse case
    worstBubble.append(timeit.timeit(lambda: bubbleSort(test1,len(test1)), number=1))
    worstQuick.append(timeit.timeit(lambda: quickSort(test2,0,len(test2)-1), number=1))
    test1 = random.sample(range(0,1000),choices[x])#bubble average, quick average, and quick best
    test2 = random.sample(range(0,1000),choices[x])#bubble average, quick average, and quick best
    averageBubble.append(timeit.timeit(lambda: bubbleSort(test1,len(test1)), number=1))
    averageQuick.append(timeit.timeit(lambda: quickSort(test2,0,len(test2)-1), number=1))
plt.scatter(choices,bestBubble,color = 'blue')
plt.scatter(choices,averageQuick,color = 'red')
plt.xlabel("length of array sorted")
plt.ylabel("Time elapsed")
plt.title("Comparison of Bubble and Quick sort best cases")
plt.legend(["Bubble","Quick"])
plt.savefig("ex2.bestCases.png")
plt.clf()
plt.scatter(choices,averageBubble,color = 'blue')
plt.scatter(choices,averageQuick,color = 'red')
plt.xlabel("length of array sorted")
plt.ylabel("Time elapsed")
plt.title("Comparison of Bubble and Quick sort average cases")
plt.legend(["Bubble","Quick"])
plt.savefig("ex2.averageCases.png")
plt.clf()
plt.scatter(choices,worstBubble,color = 'blue')
plt.scatter(choices,worstQuick,color = 'red')
plt.xlabel("length of array sorted")
plt.ylabel("Time elapsed")
plt.title("Comparison of Bubble and Quick sort worst cases")
plt.legend(["Bubble","Quick"])
plt.savefig("ex2.worstCases.png")
plt.clf()








