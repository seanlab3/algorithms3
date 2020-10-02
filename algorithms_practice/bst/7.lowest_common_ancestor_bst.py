'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a 
node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to 
the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

'''

# def lowest_common_bst(root, p, q):
#     if p > root.val and q > root.val:
#         return lowest_common_bst(root.right, p, q)
#     elif p < root.val and q < root.val:
#         return lowest_common_bst(root.left, p, q)
#     else:
#         return root.val
from algorithms3.bst import lowest_common_ancestor_bst,bst_implementation

node=bst_implementation.TreeNode(6)
node.left=bst_implementation.TreeNode(2)
node.right=bst_implementation.TreeNode(8)

node.left.left=bst_implementation.TreeNode(0)
node.left.right=bst_implementation.TreeNode(4)

node.left.left.left=bst_implementation.TreeNode(7)
node.left.left.right=bst_implementation.TreeNode(9)

node.right.left=bst_implementation.TreeNode(3)
node.right.right=bst_implementation.TreeNode(5)
p=2
q=8
a=lowest_common_ancestor_bst.lowest_common_bst(node,p,q)
print(a)
