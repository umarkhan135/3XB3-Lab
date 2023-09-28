import time 
import random
import matplotlib.pyplot as plt
from bad_sorts import create_near_sorted_list
from good_sorts import quicksort
from good_sorts import heapsort
from good_sorts import mergesort

def measure_sorting_time(algorithm, L):
    start_time = time.time()
    algorithm(L)
    end_time = time.time()
    return end_time - start_time

def experiment5():
    swap_values = range(0, 500, 10)
    list_length = 1000  
    num_runs = 10

    quick_sort_times = []
    merge_sort_times = []
    heap_sort_times = []

    for swaps in swap_values:
        quick_sort_avg_time = 0
        merge_sort_avg_time = 0
        heap_sort_avg_time = 0

        for run in range(num_runs):
            near_sorted_list = create_near_sorted_list(list_length, list_length, swaps)

            quick_list = near_sorted_list.copy()
            merge_list = near_sorted_list.copy()
            heap_list = near_sorted_list.copy()

            quick_sort_avg_time += measure_sorting_time(quicksort, quick_list)
            merge_sort_avg_time += measure_sorting_time(mergesort, merge_list)
            heap_sort_avg_time += measure_sorting_time(heapsort, heap_list)

        quick_sort_times.append(quick_sort_avg_time / num_runs)
        merge_sort_times.append(merge_sort_avg_time / num_runs)
        heap_sort_times.append(heap_sort_avg_time / num_runs)

    plt.plot(swap_values, quick_sort_times, label='Quick Sort')
    plt.plot(swap_values, merge_sort_times, label='Merge Sort')
    plt.plot(swap_values, heap_sort_times, label='Heap Sort')
    plt.xlabel('Number of Swaps')
    plt.ylabel('Average Sorting Time (seconds)')
    plt.legend()
    plt.title('Sorting Algorithm Performance')
    plt.grid()
    plt.show()
    
experiment5()
