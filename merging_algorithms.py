import searching_algorithms as s

# Input : Two arrays
# Output: merged array with unique elements
def set_union(A,B):
    C = []
    for a in A:
        if not s.linear_search(C, a):
            C.append(a)
    for b in B:
        if not s.linear_search(C, b):
            C.append(b)
    return C

# Input : Two SORTED arrays
# Output: merged array with unique elements
## uses binary search instead of linear scan
def merge_simple2(A,B):
    C = []
    for i in range(len(A)):
        if not s.binary_search(A[:i], A[i]):
            C.append(A[i])
    for i in range(len(B)):
        if not s.binary_search(A, B[i]) and not s.binary_search(B[:i], B[i]): 
            C.append(B[i])
    return C

# Input : Two SORTED arrays
# Complexity: O(n) (n = len(A) + len(B))
# Output: merged, sorted array
def merge(A,B):
    i = 0
    j = 0
    C = []
    while i < len(A) or j < len(B):
        if i < len(A) and (j >= len(B) or A[i] <= B[j]):
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            
    return C


# def median(A):
#     if len(A) ==  1:
#         return A
    
#     pivot = A[0]
#     minor = []
#     greater = []
#     for n in A:
#         if n < pivot:
#             minor.append(n)
#         elif n > pivot:
#             greater.append(n)
    
#     if len(minor) > len(greater):
#         return median(minor)
#     elif len(greater) > len(minor):
#         return median(greater)
#     else:
#         return pivot

# #median([1,2,3,4,5,6,7,8,9,10])