fname = "data.txt"
#fname = "test.txt"

import os, sys, math
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

def islist(a):
    return isinstance(a, list)

data = [ eval(x) for x in data ]

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None

def isnode(a):
    return isinstance(a, Node)

def build_tree(lst, parent, nodes):
    node = Node(parent)
    nodes.append(node)

    if islist(lst[0]):
        node.left = build_tree(lst[0], node, nodes)
    else:
        node.left = lst[0]

    if islist(lst[1]):
        node.right = build_tree(lst[1], node, nodes)
    else:
        node.right = lst[1]

    return node

def flatten_snail(node, snail = None):
    if snail == None:
        snail = []

    if isnode(node.left):
        flatten_snail(node.left, snail)
    else:
        snail.append(('L', node))

    if isnode(node.right):
        flatten_snail(node.right, snail)
    else:
        snail.append(('R', node))
    return snail

def print_snail(node):
    if isnode(node.left):
        print("[", end='')
        print_snail(node.left)
        print("]", end='')
    else:
        print(node.left, end='')

    print(",", end='')

    if isnode(node.right):
        print("[", end='')
        print_snail(node.right)
        print("]", end='')
    else:
        print(node.right, end='')

def explode(nd, level, flat_snail):
#    print(level, nd.left, " | ", nd.right)
    if isnode(nd.left):
        if explode(nd.left, level + 1, flat_snail):
            return True
    if isnode(nd.right):
        if explode(nd.right, level + 1, flat_snail):
            return True

    if level == 4:
        for i in range(len(flat_snail)):
            branch, node = flat_snail[i]
            if node == nd:
                if i > 0:
                    lbr, lnode = flat_snail[i-1]
                    if lbr == 'R':
                        lnode.right += nd.left
                    elif lbr == 'L':
                        lnode.left += nd.left
                    else:
                        raise 123

                if i < len(flat_snail) - 2:
                    lbr, lnode = flat_snail[i+2]
                    if lbr == 'R':
                        lnode.right += nd.right
                    elif lbr == 'L':
                        lnode.left += nd.right
                    else:
                        raise 123
                break

        # replace node with 0
        if nd.parent.left == nd:
            nd.parent.left = 0
        elif nd.parent.right == nd:
            nd.parent.right = 0
        else:
            raise Exception(123)

        return True
    return False

def split(node):
    if isnode(node.left):
        if split(node.left):
            return True
    else:
        if node.left > 9:
            newn = Node(node)
            newn.left = node.left // 2
            newn.right = math.ceil(node.left / 2)
            node.left = newn
            return True

    if isnode(node.right):
        if split(node.right):
            return True
    else:
        if node.right > 9:
            newn = Node(node)
            newn.left = node.right // 2
            newn.right = math.ceil(node.right / 2)
            node.right = newn
            return True
    return False

def magnitude(n):
    if isnode(n):
        magn_l = 3 * magnitude(n.left)
        magn_r = 2 * magnitude(n.right)
        return magn_l + magn_r
    else:
        return n

root = None    
for d in data:
    nodes = []
    item_root = build_tree(d, root, nodes)
    if root == None:
        root = item_root
    else:
        new_root = Node(None)
        root.parent = new_root
        item_root.parent = new_root
        new_root.left = root
        new_root.right = item_root
        root = new_root

    print_snail(root)
    print()

    while True:
        flat_snail = flatten_snail(root)
        if explode(root, 0, flat_snail) or split(root):
            #print_snail(root)
            #print()
            pass
        else:
            break

print(magnitude(root))



result=0
pyperclip.copy(result)