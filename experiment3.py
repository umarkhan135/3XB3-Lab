from bad_sorts import insertion_sort
from bad_sorts import bubble_sort
from bad_sorts import selection_sort
from bad_sorts import create_near_sorted_list

import matplotlib.pyplot as plt
import timeit

max_value = 1000000
fixed_length = 1000
swap_steps = list(range(0, fixed_length + 100, 10))

def sorting_test(sorting_algorithm, L):
    time = 0
    start = timeit.default_timer()
    sorting_algorithm(L)
    end = timeit.default_timer()
    time += end - start
    
    return time

def experiment3():

    avg_insertion_sort_times = []
    avg_bubble_sort_times = []
    avg_selection_sort_times = []
    for i in swap_steps:
        insertion_sort_time = 0 
        bubble_sort_time = 0
        selection_sort_time = 0
        for _ in range(10):
            insertion_sort_list = create_near_sorted_list(fixed_length, max_value, i)
            bubble_sort_list = insertion_sort_list.copy()
            selection_sort_list = insertion_sort_list.copy()

            insertion_sort_time += sorting_test(insertion_sort, insertion_sort_list)
            bubble_sort_time += sorting_test(bubble_sort, bubble_sort_list)
            selection_sort_time += sorting_test(selection_sort, selection_sort_list)
        
        avg_insertion_sort_times.append(insertion_sort_time/10)
        avg_bubble_sort_times.append(bubble_sort_time/10)
        avg_selection_sort_times.append(selection_sort_time/10)

    plt.plot(swap_steps, avg_insertion_sort_times, label='Insertion Sort')
    plt.plot(swap_steps, avg_bubble_sort_times, label='Bubble Sort')
    plt.plot(swap_steps, avg_selection_sort_times, label='Selection Sort')

    plt.xlabel('Number of Swap')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Insertion Sort VS Bubble Sort VS Selection Sort')
    plt.legend()
    plt.show()

experiment3()
