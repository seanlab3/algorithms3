'''
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary 
tree in which the depth of the two subtrees of every node never differ 
by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the 
following height balanced BST:

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
# def sorted_list_bst(head):
#
#     def find_middle(head):
#         slow = fast = head
#         prev = None
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
#
#         if prev: prev.next = None
#
#         return slow
#
#     if not head: return
#
#     mid = find_middle(head)
#     root = TreeNode(mid.val)
#     if head == mid: return root
#     root.left = sorted_list_bst(head)
#     root.right = sorted_list_bst(mid.next)
#
#     return root
from algorithms3.bst import list_to_bst,bst_implementation
node=list_to_bst.TreeNode(0)
node.left=list_to_bst.TreeNode(-3)
node.right=list_to_bst.TreeNode(9)

node.left.left=list_to_bst.TreeNode(-10)
node.right.left=list_to_bst.TreeNode(5)

b=list_to_bst.sorted_list_bst(node)
bst_implementation.print2D(b)
