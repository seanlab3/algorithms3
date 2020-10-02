'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# def array_bst(nums:list):
#     if not nums: return None
#
#     mid = len(nums) // 2
#     root = TreeNode(nums[mid])
#     root.left = array_bst(nums[:mid])
#     root.right = array_bst(nums[mid+1:])
#     return root
#
# def array_bst_v2(nums):
#     if not nums:
#         return None
#
#     def to_bst(left, right):
#         if left > right:
#             return None
#
#         mid = (left + right) // 2
#         node = TreeNode(nums[mid])
#         node.left = to_bst(left, mid-1)
#         node.right = to_bst(mid+1, right)
#         return node
#
#     return to_bst(0, len(nums)-1)
from algorithms3.trees import array_bst

# root=array_bst.TreeNode(0)
# root.left=array_bst.TreeNode(-3)
# root.right=array_bst.TreeNode(9)
#
# root.left.left=array_bst.TreeNode(-10)
#
# root.right.left=array_bst.TreeNode(5)
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

a=[-10,-3,0,5,9]
b=array_bst(a)
print2D(b)