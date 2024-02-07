#question 1:
#number of comparisons is = n(n-1)/2 in the average case
#for average case number of swaps we'll say that every second comparison is a swap, therefore the equation = n(n-1)/4
import random
from matplotlib import pyplot as plt
def bubbleSort(a,len):
    swaps = 0
    comparisons = 0
    for y in range(len-1):
        swap = False
        for x in range (len-1-y):
            comparisons = comparisons + 1 
            if a[x] > a[x+1]:
                swap = True
                swaps = swaps+1
                (a[x],a[x+1]) = (a[x+1],a[x])
        if swap == False:
            break
    return[swaps,comparisons]
choices = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
finalSwaps = []
finalComparisons = []
for x in choices:
    swaps = 0
    comparisons = 0
    for y in range(100):
        test = random.sample(range(0,1000),x)
        result1,result2 = bubbleSort(test,x)
        swaps = swaps + result1
        comparisons = comparisons + result2
    swaps = swaps/100
    comparisons = comparisons/100
    finalSwaps.append(swaps)
    finalComparisons.append(comparisons)
plt.scatter(choices,finalComparisons)
plt.xlabel("Number of Elements")
plt.ylabel("Number of Comparisons")
plt.title("Comparisons vs Elements")
plt.savefig("ex3.comparisonsVsElements.png")
plt.clf()
plt.scatter(choices,finalSwaps)
plt.xlabel("Number of Elements")
plt.ylabel("Number of Swaps")
plt.title("Swaps vs Elements")
plt.savefig("ex3.swapsVsElements.png")
plt.clf()
        
