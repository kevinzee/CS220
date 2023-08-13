# Discrete Structures (CSCI 220)
# Summer 2023, Session 1
# Assignment 12 - Trees and trees algorithms
# Kevin Zielinski

# Acknowledgements:
# I worked with the class.

import math
import numpy as np
import random


def random_list(n):
    l = [i for i in range(1, n + 1)]
    random.shuffle(l)
    return l


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, key):
    while root is not None:
        if key > root.data:
            root = root.right
        elif key < root.data:
            root = root.left
        else:
            return True
    return False


def insert(Node, data):
    if Node is None:
        return newNode(data)

    if data < Node.data:
        Node.left = insert(Node.left, data)
    elif data > Node.data:
        Node.right = insert(Node.right, data)
    return Node


def pre_order(root, order=None):
    if order is None:
        order = []
    if root is not None:
        order.append(root.data)
        pre_order(root.left, order)
        pre_order(root.right, order)
    return order


def in_order(root, order=None):
    if order is None:
        order = []
    if root is not None:
        in_order(root.left, order)
        order.append(root.data)
        in_order(root.right, order)
    return order


def post_order(root, order=None):
    if order is None:
        order = []
    if root is not None:
        post_order(root.left, order)
        post_order(root.right, order)
        order.append(root.data)
    return order


def reverse_order(root, order=None):
    if order is None:
        order = []
    if root is not None:
        reverse_order(root.right, order)
        order.append(root.data)
        reverse_order(root.left, order)
    return order


def DFS(root, order=None):
    if order is None:
        order = []
    if root is not None and root.data not in order:
        order.append(root.data)
        DFS(root.left, order)
        DFS(root.right, order)
    return order


def BFS(root):
    order = []
    queue = [root]
    while queue:
        v = queue.pop(0)
        if v is not None:
            order.append(v.data)
            queue.append(v.left)
            queue.append(v.right)
    return order


def level_order(root):
    return BFS(root)


def lst(root):
    return None if root is None else root.left


def rst(root):
    return None if root is None else root.right


def height(root):
    return -1 if root is None else 1 + max(height(root.left), height(root.right))


def depth(root, key):
    depth = -1
    while root is not None:
        depth += 1
        if key == root.data:
            return depth
        elif key > root.data:
            root = root.right
        elif key < root.data:
            root = root.left
    return depth


def leaves(root, lvs=None):
    if lvs is None:
        lvs = []
    if root is not None:
        if root.left is None and root.right is None:
            lvs.append(root.data)
        else:
            leaves(root.left, lvs)
            leaves(root.right, lvs)
    return lvs


def min_key(root):
    parent = root
    while root is not None:
        parent = root
        root = root.left
    return parent.data


def max_key(root):
    parent = root
    while root is not None:
        parent = root
        root = root.right
    return parent.data


def is_balanced(root):
    ll = leaves_levels(root)
    tree_levels = set()
    for l in ll:
        key = l[0]
        level = l[1]
        tree_levels.add(level)
    return len(tree_levels) <= 2


def leaves_levels(root, level=0, lvs=None):
    if lvs is None:
        lvs = []
    if root is not None:
        if root.left is None and root.right is None:
            lvs.append((root.data, level))
        else:
            leaves_levels(root.left, level + 1, lvs)
            leaves_levels(root.right, level + 1, lvs)
    return lvs


def build_tree(keys):
    root = None
    root = insert(root, keys[0])
    for i in range(1, len(keys)):
        key = keys[i]
        insert(root, key)
    return root


def main():
    keys = random_list(10)
    bst = build_tree(keys)
    for function in [pre_order, in_order, post_order, reverse_order, DFS, BFS, level_order, height, leaves,
                     min_key, max_key, is_balanced]:
        print(function.__name__, function(bst))
    print("Depth: ", keys[0], depth(bst, keys[0]))
    print("Depth: ", keys[1], depth(bst, keys[1]))
    print("Depth: ", keys[2], depth(bst, keys[2]))


if __name__ == "__main__":
    main()