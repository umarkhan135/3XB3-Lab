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
list =[7, 2, 5, 9, 1, 4, 3, 6, 8]
insertion_sort2(list)
print(list)
