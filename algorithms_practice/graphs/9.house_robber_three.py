'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, 

called the "root." Besides the root, each house has one and only one parent house. After a tour, the 
smart thief realized that "all houses in this place forms a binary tree". It will automatically contact 
the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  /     
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

'''


# def rob(root):
#
#     def dfs(node):
#         if not node: return 0, 0
#         l, r = dfs(node.left), dfs(node.right)
#         return max(l) + max(r), node.val + l[0] + r[0]
#
#     return max(dfs(root))
from algorithms3.graphs import house_robber_three

node=house_robber_three.Node(3)
node.left=house_robber_three.Node(4)
node.right=house_robber_three.Node(5)
node.left.left=house_robber_three.Node(1)
node.left.right=house_robber_three.Node(3)

node.right.right=house_robber_three.Node(1)
print(house_robber_three.rob(node))