def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def selection_sort(L):
    for i in range(0, len(L)//2):
        min_index, max_index = find_min_index(L, i)
        swap(L, i, min_index)
        swap(L, len(L) - i - 1, max_index)
        print(max_index)
        print(L)


def find_min_index(L, n):
    min_index = n
    max_index = n
    for i in range(n+1, len(L) - n):
        if L[i] < L[min_index]:
            min_index = i
        elif L[i] > L[max_index]:
            max_index = i
    return min_index, max_index


list = [7, 2, 5, 9, 1, 4, 3, 6, 8]
list2 = [2,4,3,1]
selection_sort(list)
print(list)

