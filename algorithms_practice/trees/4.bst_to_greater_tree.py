'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is 
changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

# def greater_tree(root):
#     total = 0
#
#     def inorder(root):
#         nonlocal total
#         if root:
#             inorder(root.right)
#             total += root.val
#             root.val = total
#             inorder(root.left)
#
#     inorder(root)
#     return root
#
# def greater_tree_v2(root):
#
#     def inorder(root):
#         nonlocal sums
#         if root:
#             inorder(root.left)
#             sums.append(root.val)
#             inorder(root.right)
#
#     def update(root):
#         nonlocal position, sums
#         if root:
#             update(root.left)
#             root.val = sums[position]
#             position += 1
#             update(root.right)
#
#     sums, position = [], 0
#     inorder(root)
#     for i in range(len(sums) - 2, -1, -1):
#         sums[i] += sums[i + 1]
#     update(root)
#
#     return root
class RowNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root=RowNode(5)
root.left=RowNode(2)
root.right=RowNode(13)

root2=RowNode(5)
root2.left=RowNode(2)
root2.right=RowNode(13)

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

from algorithms3.trees import bst_to_greater_tree

print2D(bst_to_greater_tree.greater_tree(root))

print2D(bst_to_greater_tree.greater_tree_v2(root2))