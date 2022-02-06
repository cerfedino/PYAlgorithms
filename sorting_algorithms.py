A = [1,6,2,4,2,3,6,12,45,876,32,12,4,668,0,-2]

# In place: YES
# Worst-case:   \Theta(n^2)
# Average-case: \Theta(n^2)
# Best-case:    \Theta(n^2)
def selection_sort(A):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]

# In place: YES
# Worst-case:   \Theta(n^2)
# Average-case: \Theta(n^2)
# Best-case:    \Theta(n)
def insertion_sort(A):
    for i in range(1,len(A)):
        value = A[i]
        j = i
        while j > 0 and A[j - 1] > value:
            A[j] = A[j-1]
            j = j - 1
        A[j] = value

# In place: YES
# Worst-case:   \Theta(n^2)
# Average-case: \Theta(n^2)
# Best-case:    \Theta(n^2)
def bubble_sort(A):
    for i in range(len(A)):
        j = len(A) - 1
        while j > i:
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
            j-= 1

# In place: NO
# Worst-case:   \Theta(nlogn)
# Average-case: \Theta(nlogn)
# Best-case:    \Theta(nlogn)
import merging_algorithms as m
def MergeSort(A):
    if len(A) == 1:
        return A
    pivot = len(A)//2
    A_left = MergeSort(A[:pivot])
    A_right = MergeSort(A[pivot:])
    return m.merge(A_left, A_right)

# In place: YES
# Worst-case:   \Theta(n^2)
# Average-case: \Theta(nlogn)
# Best-case:    \Theta(nlogn)
def quick_sort(A, begin, end):
    if end - begin >= 2:
        q = partition(A, begin, end)    # divide
        quick_sort(A, begin, q)         # conquer (right)
        quick_sort(A, q+1, end)         # conquer (left)

def partition(A, begin, end):
    assert end - begin > 1
    # pick a pivot element: deterministically A[end - 1]
    p = A[end-1]
    q = begin
    for i in range(begin, end-1):
        if A[i] < p:
            # swap A[i] an A[q]
            A[i], A[q] = A[q], A[i]
            q += 1
    A[end-1], A[q] = A[q], A[end-1]
    return q

# In place: YES
# Worst-case:   \Theta(nlogn)
# Average-case: \Theta(nlogn)
# Best-case:    \Theta(nlogn)
# TODO: Implement
def heap_sort(A):
    return A
