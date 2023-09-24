from good_sorts import *
from bad_sorts import create_random_list
import timeit

max_value = 1000000

def average(L):
    return sum(L)/len(L)

def quicksort_test():
    average_quicksort_times = []
    for i in range(0, 100000, 10000):
        time = 0
        for _ in range(10):
            L = create_random_list(i, max_value)
            start = timeit.default_timer()
            quicksort(L)
            end = timeit.default_timer()
            time += end - start
        average_quicksort_times.append(time/10)
    
    return average_quicksort_times

def mergesort_test():
    average_mergesort_times = []
    for i in range(0, 100000, 10000):
        time = 0
        for _ in range(10):
            L = create_random_list(i, max_value)
            start = timeit.default_timer()
            mergesort(L)
            end = timeit.default_timer()
            time += end - start
        average_mergesort_times.append(time/10)

    return average_mergesort_times

def heapsort_test():
    average_heapsort_times = []
    for i in range(0, 100000, 10000):
        time = 0
        for _ in range(10):
            L = create_random_list(i, max_value)
            start = timeit.default_timer()
            heapsort(L)
            end = timeit.default_timer()
            time += end - start
        average_heapsort_times.append(time/10)

    return average_heapsort_times

def experiment4():
    print(quicksort_test())
    print(mergesort_test())
    print(heapsort_test())

experiment4()
