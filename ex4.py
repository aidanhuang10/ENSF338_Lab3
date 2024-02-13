#1: When using the last element of the array for the partition value the worst possible case for quick sort arises when the partition makes no swaps
#aka the array is sorted in ascending or descending order
#when this is the case, quick sort requires n-1 total runs with n-1-runs comparisons, which ends up being the same as bubble sorts average case with n(n-1)/2

#2: a vector with 16 elements that could represent this case simply counts from 0 to 15, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] tho for demonstration purposes it is easier
#to choose a reverse sorted list [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
#after first partition the list will be [0,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
#followed by recalls with sub sections of the list ass follows [0] [14,13,12,11,10,9,8,7,6,5,4,3,2,1]
#following this trend all the way through we get
#[1,15,14,13,12,11,10,9,8,7,6,5,4,3,2]
#[1] [15,14,13,12,11,10,9,8,7,6,5,4,3,2]
#[2,15,14,13,12,11,10,9,8,7,6,5,4,3]
#[2] [15,14,13,12,11,10,9,8,7,6,5,4,3]
#[3,15,14,13,12,11,10,9,8,7,6,5,4]
#[3][15,14,13,12,11,10,9,8,7,6,5,4]
#[4,15,14,13,12,11,10,9,8,7,6,5]
#[4][15,14,13,12,11,10,9,8,7,6,5]
#[5,15,14,13,12,11,10,9,8,7,6]
#[5][15,14,13,12,11,10,9,8,7,6]
#[6,15,14,13,12,11,10,9,8,7]
#[6][15,14,13,12,11,10,9,8,7]
#[7,15,14,13,12,11,10,9,8]
#[7][15,14,13,12,11,10,9,8]
#[8,15,14,13,12,11,10,9]
#[8][15,14,13,12,11,10,9]
#[9,15,14,13,12,11,10]
#[9][15,14,13,12,11,10]
#[10,15,14,13,12,11]
#[10][15,14,13,12,11]
#[11,15,14,13,12]
#[11][15,14,13,12]
#[12,15,14,13]
#[12][15,14,13]
#[13,15,14]
#[13][15,14]
#[14,15]
#[14][15]
#resulting in the final list[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
import numpy as np
from matplotlib import pyplot as plt
import scipy
#define quadratic function for curve fitting
def func(x, a, b):
    return a * np.square(x) + b
#define partition for quick sort with comparison count
def partition(a,low,high):
    #set pivot as last element
    pivot = a[high]
    comparisons = 0
    #set current index as 1 before first element
    i = low-1
    #runs through the entire range of numbers
    for x in range(low,high):
        #if current examined number is less than or equal to the pivot
        comparisons = comparisons + 1
        if a[x] <= pivot:
            #add it into the next slot on the left side
            i = i+1
            (a[i],a[x]) = (a[x], a[i])
    #once necesesarry moves have been made put the pivot directly affter all the numbers that are smaller than it
    (a[i+1],a[high]) = (a[high],a[i+1])
    #return pivot location
    return [i+1,comparisons]
#define quicksort function with comparison counter
def quickSort(a,low,high):
    #effectivly, if the array is not size 1
    comparisons = 0
    if low<high:
        #partition the list and then recursivly call quick sort on each side of the partition
        part,comparisons = partition(a,low,high)
        comparisons = comparisons + quickSort(a,low,part-1)
        comparisons = comparisons + quickSort(a,part+1,high)
    return comparisons
choices = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
finalComparisons = []
for x in choices:
    comparisons = 0
    test = [z for z in range(x)]
    #run 100 times
    for y in range(100):
        #test is an array of x elements with numbers in order from 0 to x-1
        #get the number of comparisons made on this run
        result = quickSort(test,0,x-1)
        comparisons = comparisons + result
    #devide swaps and comparisons by 100 to get the average
    comparisons = comparisons/100
    #append results to final arrays
    finalComparisons.append(comparisons)
popt, pcov = scipy.optimize.curve_fit(func, choices, finalComparisons)
x_values = np.linspace(min(choices), max(choices), 100)
fitted_curve = func(x_values, *popt)
#plot results with modeled curves
plt.scatter(choices,finalComparisons)
plt.plot(x_values, fitted_curve)
plt.xlabel("Number of Elements")
plt.ylabel("Number of Comparisons")
plt.title("Comparisons vs Elements")
plt.show()
plt.savefig("ex4.comparisonsVsElements.png")
plt.clf()
#4: The results match our complexity analysis with a quadratic curve modling the results of comparisons against number of elements in the worst case, similar to that of the average case of bubble sort
