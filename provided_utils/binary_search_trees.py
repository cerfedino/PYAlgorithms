import sys

##############
class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None
        ###
        self.parent = None
##############

def bst_next(t):
    # next node in the natural order of keys
    if t.right != None:
        return bst_min_node(t.right)
    #
    # go up at most until we reach the root (parent == None)
    # or until the current node is the left child of its parent 
    p = t.parent
    while p != None and p.left != t:
        t = p
        p = p.parent
    return p

def bst_previous(t):
    # next node in the natural order of keys
    if t.left != None:
        return bst_max_node(t.left)
    #
    # go up at most until we reach the root (parent == None)
    # or until the current node is the right child of its parent
    p = t.parent
    while p != None and p.right != t:
        t = p
        p = p.parent
    return p


def bst_search(t, k):
    while t != None and t.key != k:
        if k > t.key:
            t = t.right
        else:
            t = t.left
    return t != None


def bst_insert(t,k):
    # insert k in t (with repetitions, i.e., in a multiset).  Return
    # the root of the tree, which is t if t != None, or a new root
    # node if t == None
    if t == None:
        return Node(k)
    r = t
    while True:
        if k <= t.key:
            if t.left == None:
                t.left = Node(k)
                return r
            else:
                t = t.left
        else:
            if t.right == None:
                t.right = Node(k)
                return r
            else:
                t = t.right