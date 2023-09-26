"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time 
from matplotlib import pyplot as plt


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
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


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
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

# ******************* Experiment 1 *******************

def Experiment1(): 
    list_lengths = [10, 100, 500, 1000, 5000]
    num_runs = 5

    bubble_time = {}
    insertion_time = {}
    selection_time = {}

    for length in list_lengths: 
        avg_bubble_time = 0
        avg_insertion_time = 0
        avg_selection_time = 0

        for run in range(num_runs):
            random_list = create_random_list(length, 1000)

            start_time = time.time()
            bubble_sort(random_list.copy())
            end_time = time.time()
            avg_bubble_time += (end_time - start_time)

            start_time = time.time()
            insertion_sort(random_list.copy())
            end_time = time.time()
            avg_insertion_time += (end_time - start_time)

            start_time = time.time()
            selection_sort(random_list.copy())
            end_time = time.time()
            avg_selection_time += (end_time - start_time)

        avg_bubble_time /= num_runs
        avg_insertion_time /= num_runs
        avg_selection_time /= num_runs

        bubble_time[length] = avg_bubble_time
        insertion_time[length] = avg_insertion_time
        selection_time[length] = avg_selection_time

    print(bubble_time)
    print(insertion_time)
    print(selection_time)

    plt.plot(list_lengths, list(bubble_time.values()), label="Bubble Sort")
    plt.plot(list_lengths, list(insertion_time.values()), label="Insertion Sort")
    plt.plot(list_lengths, list(selection_time.values()), label="Selection Sort")

    plt.xlabel("List Length")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.show()

