import timeit
import matplotlib.pyplot as plot
import random


def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L,i)
    

def insert2(L,i):
    temp = L[i]
    while i > 0 and temp < L[i-1]:
        L[i] = L[i-1]
        i -= 1
    L[i] = temp


'''
def insertion_sort2v2(L):
    for i in range(1, len(L)):
        insert3(L,i)
        
def insert3(L,i):
    temp = L[i]
    while i > 0:
        print(i)
        print(L)
        if temp < L[i-1]:
            L[i] = L[i-1]
            i-= 1
        elif L[i] == L[i+1]:
            L[i] = temp
        else:
            return
'''

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

def graphing(n):
    times = []
    times2 = []
    for i in range(n):
        list = create_random_list(1000,1000)
        list2 = list.copy()
        
        start1 = timeit.default_timer()
        insertion_sort(list)
        total = timeit.default_timer() - start1
        times.append(total)
        
        start2 = timeit.default_timer()
        insertion_sort2(list2)
        total2 = timeit.default_timer() - start2
        times2.append(total2)
    return times,times2
        
time = graphing(1000)
plot.plot(time[0], label='Insertion Sort')
plot.plot(time[1], label='Insertion Sort 2')
plot.legend()
plot.show()

