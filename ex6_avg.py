import timeit
import random 
import numpy as np
from matplotlib import pyplot as plt
import scipy
#Linear Search 
def linearSearch (arr, n, key):
    for i in range(n):
        if key == arr[i]:
            return i
    return -1 #Key was not found in array

vector1 = random.sample(range(0, 10000), 100)
vector2 = random.sample(range(0, 10000), 200)
vector3 = random.sample(range(0, 10000), 400)
vector4 = random.sample(range(0, 10000), 800)
vector5 = random.sample(range(0, 10000), 1600)
vector6 = random.sample(range(0, 10000), 3200)