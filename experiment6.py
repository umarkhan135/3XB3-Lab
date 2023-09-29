import random

def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def quicksort_copy(L):
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
    return quicksort_copy(left) + quicksort_copy(middle) +  quicksort_copy(right)


def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

list = create_random_list(10, 100)
quicksort(list)
print(list)