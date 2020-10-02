'''
Given a binary search tree with non-negative values, find the minimum absolute difference between 
values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
'''

# def min_diff_bst(root):
# # #
# # #     def inorder(root):
# # #         nonlocal prev, minimum
# # #         if root:
# # #             inorder(root.left)
# # #             if prev:
# # #                 minimum = min(minimum, root.val - prev.val)
# # #             prev = root
# # #             inorder(root.right)
# # #
# # #     prev, minimum = None, float('inf')
# # #     inorder(root)
# # #     return minimum

from algorithms3.bst import bst_implementation,minimum_diff_bst

node=bst_implementation.TreeNode(1)

node.right=bst_implementation.TreeNode(3)

node.right.left=bst_implementation.TreeNode(2)

print(minimum_diff_bst.min_diff_bst(node))