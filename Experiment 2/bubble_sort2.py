import time
import matplotlib.pyplot as plt
import random



def measure_execution_time(sort_func, test_list, num_runs):
    total_time = 0
    for _ in range(num_runs):
        list_copy = test_list.copy()
        start_time = time.time()
        sort_func(list_copy)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / num_runs

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]



def bubble_sort3(L):
    for i in range(len(L)//2):
        bubble_up2(L,0)



def bubble_up2(L, i):
    current = L[i]
    while i < len(L) - 1:
        if current > L[i + 1]:
            L[i] = L[i + 1]
        else:
            L[i] = current
            current = L[i + 1]
            i += 1
            continue
        i += 1
    L[i] = current

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
    
    

def experiment2_bubble():
    
    runs = 50
    list_lengths = list(range(10, 1000, 10))
    buublesort_times = []
    bubble_sort2_times = []
    max_value = 1000
    
    for i in list_lengths:
        random_list = create_random_list(i, max_value)
        
        buublesort_times.append(measure_execution_time(bubble_sort, random_list, runs))
        bubble_sort2_times.append(measure_execution_time(bubble_sort3, random_list, runs))
        
    plt.plot(list_lengths, buublesort_times, label='Bubble Sort')
    plt.plot(list_lengths, bubble_sort2_times, label='Bubble Sort 2')
    plt.xlabel('List Length')
    plt.ylabel('Average Execution Time (s)')
    plt.title('Bubble Sort VS Bubble Sort 2')
    plt.legend()
    plt.grid(True)
    plt.show()
    

