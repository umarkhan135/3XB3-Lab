import time
import matplotlib.pyplot as plt
import random
from bubble_sort2 import measure_execution_time

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

def selection_sort2(L):
    for i in range(0, len(L)//2):
        min_index, max_index = find_min_index2(L, i)
        if min_index != len(L) - i:
            swap(L, i, min_index)
        swap(L, len(L) - i - 1, max_index)
        
        
        


def find_min_index2(L, n):
    min_index = n
    max_index = len(L) - n - 1
    for i in range(n+1, len(L) - n):
        if L[i] < L[min_index]:
            min_index = i
        elif L[i] > L[max_index]:
            max_index = i
    return min_index, max_index


def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


def experiment2_selection():
    
    runs = 50
    list_lengths = list(range(10, 1000, 10))
    selectionsort_times = []
    selection_sort2_times = []
    max_value = 1000
    
    for i in list_lengths:
        random_list = create_random_list(i, max_value)
        
        selectionsort_times.append(measure_execution_time(selection_sort, random_list, runs))
        selection_sort2_times.append(measure_execution_time(selection_sort2, random_list, runs))
        
    plt.plot(list_lengths, selectionsort_times, label='Selection Sort')
    plt.plot(list_lengths, selection_sort2_times, label='Selection Sort 2')
    plt.xlabel('List Length')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Selection Sort VS Selection Sort 2')
    plt.legend()
    plt.grid(True)
    plt.show()
    
