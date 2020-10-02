'''
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
'''

# class BSTNodeInsert:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# def insert_to_bst(root, val):
#     if root == None:
#         root = BSTNodeInsert(val)
#     else:
#         if root.val < val:
#             if root.right == None:
#                 root.right = BSTNodeInsert(val)
#             else:
#                 insert_to_bst(root.right, val)
#         else:
#             if root.left == None:
#                 root.left = BSTNodeInsert(val)
#             else:
#                 insert_to_bst(root.left, val)
#
#     return root
#
# def insert_to_bst_v2(root, val):
#     if root == None:
#         root = BSTNodeInsert(val)
#         return root
#
#     current = root
#     while True:
#         if current.val < val:
#             if current.right is None:
#                 current.right = BSTNodeInsert(val)
#                 return root
#             current = current.right
#         else:
#             if current.left is None:
#                 current.left = BSTNodeInsert(val)
#                 return root
#             current = current.left
#
#     return -1

from algorithms3.bst import insert_into_bst,bst_implementation

node=insert_into_bst.BSTNodeInsert(4)
node.left=insert_into_bst.BSTNodeInsert(2)
node.right=insert_into_bst.BSTNodeInsert(7)

node.left.left=insert_into_bst.BSTNodeInsert(1)
node.left.right=insert_into_bst.BSTNodeInsert(3)

a=insert_into_bst.insert_to_bst(node,5)

b=insert_into_bst.insert_to_bst_v2(node,5)
bst_implementation.print2D(a)
bst_implementation.print2D(b)

