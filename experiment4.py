from good_sorts import quicksort
from good_sorts import mergesort
from good_sorts import heapsort
from bad_sorts import create_random_list

import matplotlib.pyplot as plt
import timeit

max_value = 1000000
list_lengths = list(range(0, 31000, 1000))

def sorting_test(sorting_algorithm, L):
    time = 0
    start = timeit.default_timer()
    sorting_algorithm(L)
    end = timeit.default_timer()
    time += end - start
    
    return time
    
def experiment4():
    avg_quicksort_times = []
    avg_mergesort_times = []
    avg_heapsort_times = []
    for i in list_lengths:
        quicksort_time = 0
        mergesort_time = 0
        heapsort_time = 0
        for _ in range(10):
            quicksort_list = create_random_list(i, max_value)
            mergesort_list = quicksort_list.copy()
            heapsort_list = quicksort_list.copy()

            quicksort_time += sorting_test(quicksort, quicksort_list)
            mergesort_time += sorting_test(mergesort, mergesort_list)
            heapsort_time += sorting_test(heapsort, heapsort_list)
        
        avg_quicksort_times.append(quicksort_time/10)
        avg_mergesort_times.append(mergesort_time/10)
        avg_heapsort_times.append(heapsort_time/10)

    plt.plot(list_lengths, avg_quicksort_times, label='Quick Sort')
    plt.plot(list_lengths, avg_mergesort_times, label='Merge Sort')
    plt.plot(list_lengths, avg_heapsort_times, label='Heap Sort')

    plt.xlabel('List Length')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Quicksort VS Mergesort VS Heapsort')
    plt.legend()
    plt.show()

experiment4()
