import timeit
import random
from matplotlib import pyplot as plt
#create bubble sort function
def bubbleSort(a,len):
    #runs once for every element in the array - 1
    for y in range(len-1):
        swaps = False
        #runs once for every element in the array minus the number of outside loop runs
        for x in range (len-1-y):
            #if current element is greater than next element swap them
            if a[x] > a[x+1]:
                swaps = True
                (a[x],a[x+1]) = (a[x+1],a[x])
        #if no swaps were made this run then the array is sorted
        if swaps == False:
            break
#create partition function
def partition(a,low,high):
    #set pivot as last element
    pivot = a[high]
    #set current index as 1 before first element
    i = low-1
    #runs through the entire range of numbers
    for x in range(low,high):
        #if current examined number is less than or equal to the pivot
        if a[x] <= pivot:
            #add it into the next slot on the left side
            i = i+1
            (a[i],a[x]) = (a[x], a[i])
    #once necesesarry moves have been made put the pivot directly affter all the numbers that are smaller than it
    (a[i+1],a[high]) = (a[high],a[i+1])
    #return pivot location
    return i+1
#define quicksort function
def quickSort(a,low,high):
    #effectivly, if the array is not size 1
    if low<high:
        #partition the list and then recursivly call quick sort on each side of the partition
        part = partition(a,low,high)
        quickSort(a,low,part-1)
        quickSort(a,part+1,high)
#sizes of choice: 2,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50,75,100,125,150
#create lists to hold results
bestBubble = []
worstBubble = []
averageBubble = []
worstQuick = []
averageQuick = []
choices = [2,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50,75,100,125,150]
for x in range(20):#run once for each choice
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
#plot results 
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
#question 4:
#looking at the plots, in all but the best cases it appears that quick sort becomes faster
#than bubble sort around 10 elements, so a small sort would have 9 or less elements 








