# Complexity: n
def linear_search(A,x):
    for i in A:
        if i == x:
            return True
    return False

# Input: sorted sequence
# complexity: nlogn
def binary_search(A,x):
    begin = 0
    end = len(A)
    while begin < end:

        # picks index in the middle
        m = (begin + end) // 2
        if A[m] == x:
            return True
        elif A[m] > x:
            end = m
        else:
            begin = m + 1   # Why '+ 1'
    return False