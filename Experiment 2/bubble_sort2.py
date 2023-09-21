def bubble_sort2(L):
    for i in range(len(L)):
        bubble_up(L, i)

def bubble_sort3(L):
    for i in range(len(L)):
        bubble_up2(L, i)

def bubble_up(L, i):
    current = L[i]
    while i < len(L) - 1 and current > L[i + 1]:
        L[i] = L[i + 1]
        i += 1
    L[i] = current

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

list = [7, 2, 5, 9, 1, 4, 3, 6, 8]
bubble_sort2(list)
print(list)

list = [7, 2, 5, 9, 1, 4, 3, 6, 8]
bubble_sort3(list)
print(list)
