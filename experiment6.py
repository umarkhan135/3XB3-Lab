import random
from good_sorts import quicksort
from Experiment8 import measure_execution_time
import matplotlib.pyplot as plt


def dual_quicksort(L):
    copy = quicksort_copy2(L)
    for i in range(len(L)):
        L[i] = copy[i]


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def quicksort_copy2(L):
    if len(L) <= 1:
        return L
    pivot1 = L[0]
    pivot2 = L[-1]
    
    if len(L) == 2:
        if L[0] <= L[1]:
            return L
        elif L[0] > L[1]:
            swap(L, 0, 1)
         
    i = 0   
    while pivot2 == pivot1 and len(L) > 1 and i < len(L) - 1:
        pivot2 = L[-1 - i]
        i += 1
    
    if pivot2 == pivot1:
        return L

            
    if pivot1 > pivot2:
        pivot1, pivot2 = pivot2, pivot1
        
    left, right, middle = [], [], []
    for num in L:
        if num < pivot1:
            left.append(num)
        elif pivot1 <= num < pivot2:
            middle.append(num)
        else:
            right.append(num)
    return quicksort_copy2(left) + quicksort_copy2(middle) +  quicksort_copy2(right)


def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

    
def experiment6():
    
    runs = 5
    list_lengths = list(range(100, 100000, 1000))
    quicksort_times = []
    dual_quicksort_times = []
    max_value = 1000
    
    for i in list_lengths:
        random_list = create_random_list(i, max_value)
        
        quicksort_times.append(measure_execution_time(quicksort, random_list, runs))
        dual_quicksort_times.append(measure_execution_time(dual_quicksort, random_list, runs))
        
    plt.plot(list_lengths, quicksort_times, label='Quick Sort')
    plt.plot(list_lengths, dual_quicksort_times, label='Dual Quick Sort')
    plt.xlabel('List Length')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Quick Sort VS Dual Quick Sort')
    plt.legend()
    plt.grid(True)
    plt.show()
    
