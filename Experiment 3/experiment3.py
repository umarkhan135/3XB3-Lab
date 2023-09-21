from bad_sorts import create_near_sorted_list

import timeit
import random
import matplotlib.pyplot as plt

def experiment3():
    times = []
    for i in range(100000, 1000000, 100000):
        L = create_near_sorted_list(1000000, 1000000, i)
        L1 = L.copy(); L2 = L.copy()
