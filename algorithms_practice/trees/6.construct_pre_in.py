'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# def build_tree_inpre(preorder, inorder):
#     inorder_hash = {}
#     for i, e in enumerate(inorder):
#         inorder_hash[e] = i
#     pre_index = [0]
#     def build(start, end, inorder, preorder):
#         if start > end:
#             return None
#
#         new_node = TreeNode(preorder[pre_index[0]])
#         pre_index[0] += 1
#
#         if start == end:
#             return new_node
#
#         index = inorder_hash[new_node.val]
#         new_node.left = build(start, index-1, inorder, preorder)
#         new_node.right = build(index+1, end, inorder, preorder)
#
#         return new_node
#
#     return build(0, len(inorder)-1, inorder, preorder)

# preorder=TreeNode(3)
# preorder.left=TreeNode(9)
# preorder.right=TreeNode(20)
#
# preorder.right.left=TreeNode(15)
# preorder.right.right=TreeNode(7)
#
# inorder=TreeNode(9)
# inorder.left=TreeNode(3)
# inorder.right=TreeNode(15)
#
# inorder.right.left=TreeNode(20)
# inorder.right.right=TreeNode(7)
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

from algorithms3.trees import construct_pre_in
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
a=construct_pre_in.build_tree_inpre(preorder,inorder)
print2D(a)
