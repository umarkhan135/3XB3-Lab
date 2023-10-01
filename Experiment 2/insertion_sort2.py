import time
import matplotlib.pyplot as plt
import random
from bubble_sort2 import measure_execution_time



def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L,i)
    

def insert2(L,i):
    temp = L[i]
    while i > 0 and temp < L[i-1]:
        L[i] = L[i-1]
        i -= 1
    L[i] = temp


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]
    
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return

def experiment2_insertion():
    
    runs = 50
    list_lengths = list(range(10, 1000, 10))
    insertionsort_times = []
    insertion_sort2_times = []
    max_value = 1000
    
    for i in list_lengths:
        random_list = create_random_list(i, max_value)
        
        insertionsort_times.append(measure_execution_time(insertion_sort, random_list, runs))
        insertion_sort2_times.append(measure_execution_time(insertion_sort2, random_list, runs))
        
    plt.plot(list_lengths, insertionsort_times, label='Insertion Sort')
    plt.plot(list_lengths, insertion_sort2_times, label='Insertion Sort 2')
    plt.xlabel('List Length')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Insertion Sort VS Insertion Sort 2')
    plt.legend()
    plt.grid(True)
    plt.show()
    

