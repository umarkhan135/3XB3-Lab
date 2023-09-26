import timeit
import matplotlib.pyplot as plot
import random

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# def bubble_sort2(L):
#     for i in range(len(L)):
#         bubble_up(L, i)

def bubble_sort3(L):
    for i in range(len(L)//2):
        bubble_up2(L,0)

# def bubble_up(L, i):
#     current = L[i]
#     while i < len(L) - 1 and current > L[i + 1]:
#         L[i] = L[i + 1]
#         i += 1
#     L[i] = current

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
    
    

def graphing(n):
    times = []
    times2 = []
    for i in range(n):
        list = create_random_list(1000,1000)
        list2 = list.copy()
        
        start1 = timeit.default_timer()
        bubble_sort(list)
        total = timeit.default_timer() - start1
        times.append(total)
        
        start2 = timeit.default_timer()
        bubble_sort3(list2)
        total2 = timeit.default_timer() - start2
        times2.append(total2)
    return times,times2
        
time = graphing(1000)
plot.plot(time[0], label='Bubble Sort')
plot.plot(time[1], label='Bubble Sort 2')
plot.legend()
plot.show()
