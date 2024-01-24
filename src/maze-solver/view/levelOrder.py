# Recursive Python program for level
# order traversal of Binary Tree
# A node structure
from __future__ import annotations


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)


# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=' ')
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)


# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printLevelOrder(rtt):
    # Base Case
    if rtt is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(rtt)

    while len(queue) > 0:
        # Print front of queue and
        # remove it from queue
        print(queue[0].val, end=' ')
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver program to test above function
if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(1)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.left.left.left = Node(0)
    root.left.left.right = Node(0)
    root.left.right.left = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(0)
    root.left.right.right = Node(1)
    print('Level order traversal of binary tree is -')

    """
    rt = TreeNode(2)
    rt.left = TreeNode(1)

    rt.left.left = TreeNode(1)
    rt.left.right = TreeNode(2)
    rt.right = TreeNode(7)
    rt.right.left = TreeNode(12)
    rt.right.right = TreeNode(8)
    printLevelOrder(rt)
    """
    n = 0
    root = TreeNode(n)
    n += 1
    l = root
    last = 'right'
    for i in range(100)[1:]:
        if not l.left:
            l.left = TreeNode(i)
        elif not l.right:
            l.right = TreeNode(i)
            last = 'right' if last == 'left' else 'left'
            i += 1
        l = l.right
        if not l.left:
            l.left = TreeNode(i)
        elif not l.right:
            l.right = TreeNode(i)
            last = 'right' if last == 'left' else 'left'
            i += 1

    printLevelOrder(root)
