'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the 
BST such that their sum is equal to the given target.
'''

# def find_target(root, k):
#     traversal = []
#
#     def inorder(root):
#         nonlocal traversal
#         if root:
#             inorder(root.left)
#             traversal.append(root.val)
#             inorder(root.right)
#
#     inorder(root)
#     left, right = 0, len(traversal) - 1
#     while left < right:
#         sumx = traversal[left] + traversal[right]
#         if sumx == k:
#             return True
#         elif sumx < k:
#             left += 1
#         else:
#             right -= 1
#
#     return False
from algorithms3.bst import two_sum_bst,bst_implementation
node=bst_implementation.TreeNode(4)
node.left=bst_implementation.TreeNode(2)
node.right=bst_implementation.TreeNode(7)
node.left.left=bst_implementation.TreeNode(1)
node.left.right=bst_implementation.TreeNode(3)

a=two_sum_bst.search_bst_v1(node,2)
bst_implementation.print2D(a)