import random

def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L


def bottom_up_mergesort(L):
    part = 1
    length = len(L)
    while part < length:
        for i in range(0, length, part * 2):
            left = L[i: i + part]
            right = L[i + part: i + part * 2]
            L[i:i + part * 2] = merge(left, right)
        part = part * 2

'''
# Testing the bottom_up_mergesort function
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

list = create_random_list(19, 100)
bottom_up_mergesort(list)
print(list)
'''