import timeit
import matplotlib.pyplot as plot
import random

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


def graphing(n):
    times = []
    times2 = []
    for i in range(n):
        list = create_random_list(1000,1000)
        list2 = list.copy()
        
        start1 = timeit.default_timer()
        selection_sort(list)
        total = timeit.default_timer() - start1
        times.append(total)
        
        start2 = timeit.default_timer()
        selection_sort2(list2)
        total2 = timeit.default_timer() - start2
        times2.append(total2)
    return times,times2
        
time = graphing(1000)
plot.plot(time[0], label='Selection Sort')
plot.plot(time[1], label='Selection Sort 2')
plot.legend()
plot.show()
