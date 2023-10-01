import random
from good_sorts import mergesort
from Experiment8 import measure_execution_time
import matplotlib.pyplot as plt
from bad_sorts import create_random_list


def merge2(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L


def bottom_up_mergesort(L):
    part = 1
    length = len(L)
    while part < length:
        for i in range(0, length, part * 2):
            left = L[i: i + part]
            right = L[i + part: i + part * 2]
            L[i:i + part * 2] = merge2(left, right)
        part = part * 2

def experiment7():
    
    runs = 5
    list_lengths = list(range(100, 100000, 1000))
    mergesort_times = []
    bottom_up_mergesort_times = []
    max_value = 1000
    
    for i in list_lengths:
        random_list = create_random_list(i, max_value)
        
        mergesort_times.append(measure_execution_time(mergesort, random_list, runs))
        bottom_up_mergesort_times.append(measure_execution_time(bottom_up_mergesort, random_list, runs))
        
    plt.plot(list_lengths, mergesort_times, label='Merge Sort')
    plt.plot(list_lengths, bottom_up_mergesort_times, label='Bottom Up Merge Sort')
    plt.xlabel('List Length')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Merge Sort VS Bottom Up Merge Sort')
    plt.legend()
    plt.grid(True)
    plt.show()
    
