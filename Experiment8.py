import random
import time
import matplotlib.pyplot as plt
from good_sorts import mergesort
from good_sorts import quicksort
from bad_sorts import insertion_sort
from bad_sorts import create_random_list

def measure_execution_time(sort_func, test_list, num_runs):
    total_time = 0
    for _ in range(num_runs):
        list_copy = test_list.copy()
        start_time = time.time()
        sort_func(list_copy)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / num_runs

def experiment8():
    list_lengths = list(range(10, 101, 10))
    num_runs = 1000
    max_value = 1000  

    insertion_sort_times = []
    merge_sort_times = []
    quicksort_times = []

    for length in list_lengths:
        random_list = create_random_list(length, max_value)
        
        insertion_sort_times.append(measure_execution_time(insertion_sort, random_list, num_runs))
        merge_sort_times.append(measure_execution_time(mergesort, random_list, num_runs))
        quicksort_times.append(measure_execution_time(quicksort, random_list, num_runs))

    plt.plot(list_lengths, insertion_sort_times, label='Insertion Sort')
    plt.plot(list_lengths, merge_sort_times, label='Merge Sort')
    plt.plot(list_lengths, quicksort_times, label='Quicksort')

    plt.xlabel('List Length')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Sorting Algorithm Comparison for Random Lists')
    plt.legend()
    plt.grid(True)
    plt.show()

experiment8()