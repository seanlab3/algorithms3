'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 /   /
4  5 6

Output: 6
'''

# def count_nodes(root):
#     def left_depth(root):
#         if root is None: return 0
#         return 1 + left_depth(root.left)
#
#     def count(root):
#         if root is None: return 0
#         left = left_depth(root.left)
#         right = left_depth(root.right)
#         if left > right:
#             return 2 ** right + count(root.left)
#         else:
#             return 2 ** left + count(root.right)
#
#     return count(root)
#
#
# def count_nodes_v2(root):
#     if root is None: return 0
#     return 1 + count_nodes(root.left) + count_nodes(root.right)

COUNT = [10]
def print2DUtil(root, space) :

    # Base case
    if (root == None) :
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)

# Wrapper over print2DUtil()
def print2D(root) :

    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)

class RowNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root=RowNode(1)
root.left=RowNode(2)
root.right=RowNode(3)

root.left.left=RowNode(4)
root.left.right=RowNode(5)

root.right.left=RowNode(6)

from algorithms3.trees import count_complete_tree_nodes
a=count_complete_tree_nodes.count_nodes(root)
print2D(a)
