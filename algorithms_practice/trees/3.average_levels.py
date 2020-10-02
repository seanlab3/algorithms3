'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''
# from collections import deque
#
# def average_levels(root):
#     if root is None:
#         return []
#
#     que = deque()
#     que.append(root)
#     result = []
#
#     while len(que) > 0:
#         sumx = 0
#         count = 0
#         for _ in range(len(que)):
#             current = que.popleft()
#             sumx += current.val
#             count += 1
#             if current.left: que.append(current.left)
#             if current.right: que.append(current.right)
#
#         result.append(sumx/count)
#     return result
class RowNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
root=RowNode(3)
root.left=RowNode(9)
root.right=RowNode(20)

root.right.left=RowNode(15)
root.right.right=RowNode(7)
from algorithms3.trees import average_levels

print(average_levels(root))