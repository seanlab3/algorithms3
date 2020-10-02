'''
Given the root node of a binary search tree, return the sum of values of all nodes with value 
between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
'''

# def range_sum_bst(root, L, R):
# # #     sumx = 0
# # #
# # #     def dfs(root):
# # #         nonlocal sumx
# # #         if root and L <= root.val <= R:
# # #             sumx += root.val
# # #             dfs(root.left)
# # #             dfs(root.right)
# # #         elif root and root.val < L:
# # #             dfs(root.right)
# # #         elif root and root.val > R:
# # #             dfs(root.left)
# # #
# # #     dfs(root)
# # #     return sumx
# # #
# # #
# # # def range_sum_bst_v2(root, L, R):
# # #     sumx = 0
# # #
# # #     def inorder(root):
# # #         nonlocal sumx
# # #         if root:
# # #             inorder(root.left)
# # #             if L <= root.val <= R: sumx += root.val
# # #             inorder(root.right)
# # #
# # #     inorder(root)
# # #     return sumx
from algorithms3.bst import range_sum_bst,bst_implementation

node=bst_implementation.TreeNode(10)
node.left=bst_implementation.TreeNode(5)
node.right=bst_implementation.TreeNode(15)

node.left.left=bst_implementation.TreeNode(3)
node.left.right=bst_implementation.TreeNode(7)

node.right.right=bst_implementation.TreeNode(18)

L=7
R=15
print(range_sum_bst.range_sum_bst_v1(node,L,R))

print(range_sum_bst.range_sum_bst_v2(node,L,R))