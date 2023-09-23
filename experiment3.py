from bad_sorts import *

import timeit

max_value = 1000000
fixed_length = 10000
step = 1000

def average(L):
    return sum(L)/len(L)

def insertion_sort_test():  
    average_insertion_sort_times = []
    for _ in range(10):
        insertion_sort_times = []
        for i in range(1000, fixed_length, step):
            time = 0
            L = create_near_sorted_list(fixed_length, max_value, i)
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            time += end - start
            insertion_sort_times.append(time)
        average_insertion_sort_times.append(average(insertion_sort_times))
    
    return average_insertion_sort_times

def bubble_sort_test():  
    average_bubble_sort_times = []
    for _ in range(10):
        bubble_sort_times = []
        for i in range(1000, fixed_length, step):
            time = 0
            L = create_near_sorted_list(fixed_length, max_value, i)
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            time += end - start
            bubble_sort_times.append(time)
        average_bubble_sort_times.append(average(bubble_sort_times))
    
    return average_bubble_sort_times

def selection_sort_test():  
    average_selection_sort_times = []
    for _ in range(10):
        selection_sort_times = []
        for i in range(1000, fixed_length, step):
            time = 0
            L = create_near_sorted_list(fixed_length, max_value, i)
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            time += end - start
            selection_sort_times.append(time)
        average_selection_sort_times.append(average(selection_sort_times))
    print(average_selection_sort_times)

def experiment3():
    print(insertion_sort_test())
    print(bubble_sort_test())
    print(selection_sort_test())

experiment3()
