'''
Given the root of a binary search tree with distinct values, modify it so that every node has a new value 
equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 

Note:

The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
'''

# def bst_to_greater(root):
#     largest = 0
#
#     def inorder(root):
#         nonlocal largest
#         if root is None: return
#         if root.right: inorder(root.right)
#         root.val += largest
#         largest = root.val
#         if root.left: inorder(root.left)
#
#     inorder(root)
#     return root
from algorithms3.bst import bst_to_greater_sum_tree,bst_implementation

# root = Node(4)
# root.left = Node(2)
# root.right = Node(5)
# root.left.left = Node(1)
# root.left.right = Node(3)

node=bst_implementation.TreeNode(4)
node.left=bst_implementation.TreeNode(1)
node.right=bst_implementation.TreeNode(6)

node.left.left=bst_implementation.TreeNode(0)
node.left.right=bst_implementation.TreeNode(2)

node.left.right.right=bst_implementation.TreeNode(33)

node.right.left=bst_implementation.TreeNode(5)
node.right.right=bst_implementation.TreeNode(7)

node.right.right.right=bst_implementation.TreeNode(7)


a=bst_to_greater_sum_tree(node)
bst_implementation.print2D(a)


