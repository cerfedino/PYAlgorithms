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

def right_rotate (t):
    assert t != None and t.left != None
    r = t.left
    t.left = r.right
    r.right = t
    return r

def left_rotate (t):
    assert t != None and t.right != None
    r = t.right
    t.right = r.left
    r.left = t
    return r

# Example BST
# t = Node(5)
# t.left = Node(3)
# t.left.left = Node(2)
# t.left.right = Node(4)
# t.right = Node(7)
# t.right.right = Node(8)
# t.right.right.right = Node(9)

def bst_min_node(t):
    if t == None:
        return None
    while t.left != None:
        t = t.left
    return t

def bst_max_node(t):
    if t == None:
        return None
    while t.right != None:
        t = t.right
    return t


# To find the minimum, we go as far left as possible.
def bst_min(t):                 # minimum key in t
    if t == None:
        return None
    while t.left != None:
        t = t.left
    return t.key

# To find the maximum, we go as far right as possible
def bst_max(t):                 # maximum key in t
    if t == None:
        return None
    while t.right != None:
        t = t.right
    return t.key

# Returns number of nodes
def bst_size(t):
    if t == None:
        return 0
    else:
        return bst_size(t.left) + 1 + bst_size(t.right)

# Returns height of tree
def bst_height(t):
    if t == None:
        return 0
    else:
        return 1 + max(bst_height(t.left), bst_height(t.right))

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


def bst_straighten(t):
    while t.left != None:
        t = right_rotate(t)
    n = t
    while n.right != None:
        n = n.right
        while n.left != None:
            n = right_rotate(n)
    return t


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

#def bst_delete(t,k):