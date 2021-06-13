import sys
import provided_utils.print_binary_tree as pr
##############
class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None
        ###
        self.parent = None
##############

def build_max_heap_graph(A):
    return build_max_heap_graph_r(A,1)

def build_max_heap_graph_r(A, k):
    if k > len(A):
        return None
    
    t = Node(A[k-1])
    t.left = build_max_heap_graph_r(A, k*2)
    t.right = build_max_heap_graph_r(A, (k*2)+1)

    return t

# A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]