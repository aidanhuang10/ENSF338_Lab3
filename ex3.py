#question 1:
#number of comparisons is = n(n-1)/2 in the average case
#for average case number of swaps we'll say that every second comparison is a swap, therefore the equation = n(n-1)/4
import random
from matplotlib import pyplot as plt
import numpy as np
import scipy
#define quadratic function for curve fitting
def func(x, a, b):
    return a * np.square(x) + b
#define bubble sort with comparison and swap counters
def bubbleSort(a,len):
    swaps = 0
    comparisons = 0
    #runs once for each element in the array minus 1
    for y in range(len-1):
        swap = False
        #runs once for each element in the array minus the number of times the outside loop has ran minus 1
        for x in range (len-1-y):
            comparisons = comparisons + 1 
            #if current element is bigger than the next element swap them
            if a[x] > a[x+1]:
                swap = True
                swaps = swaps+1
                (a[x],a[x+1]) = (a[x+1],a[x])
        #if no swaps were made then array is sorted
        if swap == False:
            break
        #return the number of swaps and comparisons made
    return[swaps,comparisons]
#define choices for array size and total swaps and comparisons
choices = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
finalSwaps = []
finalComparisons = []
#for each array length that was decided upon
for x in choices:
    swaps = 0
    comparisons = 0
    #run 100 times
    for y in range(100):
        #test is an array of x elements with numbers from 0 to 1000
        test = random.sample(range(0,1000),x)
        #get the number of comparisons made on this run
        result1,result2 = bubbleSort(test,x)
        swaps = swaps + result1
        comparisons = comparisons + result2
    #devide swaps and comparisons by 100 to get the average
    swaps = swaps/100
    comparisons = comparisons/100
    #append results to final arrays
    finalSwaps.append(swaps)
    finalComparisons.append(comparisons)
#create curves to model results
popt, pcov = scipy.optimize.curve_fit(func, choices, finalComparisons)
popt2, pcov2 = scipy.optimize.curve_fit(func, choices, finalSwaps)
x_values = np.linspace(min(choices), max(choices), 100)
fitted_curve = func(x_values, *popt)
fitted_curve2 = func(x_values, *popt2)
#plot results with modeled curves
plt.scatter(choices,finalComparisons)
plt.plot(x_values, fitted_curve)
plt.xlabel("Number of Elements")
plt.ylabel("Number of Comparisons")
plt.title("Comparisons vs Elements")
plt.savefig("ex3.comparisonsVsElements.png")
plt.clf()
plt.scatter(choices,finalSwaps)
plt.plot(x_values, fitted_curve2)
plt.xlabel("Number of Elements")
plt.ylabel("Number of Swaps")
plt.title("Swaps vs Elements")
plt.savefig("ex3.swapsVsElements.png")
plt.clf()
#4: Both fitted curves match our complexity analysis with quadratic curves successfully modeling the results
        
