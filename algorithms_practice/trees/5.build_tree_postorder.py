'''Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# def build_tree_postorder(inorder, postorder):
#     inorder_hash = {}
#     for i, e in enumerate(inorder):
#         inorder_hash[e] = i
#     post_index = [len(postorder)-1]
#
#     def build(start, end, inorder, postorder):
#         if start > end:
#             return None
#
#         new_node = TreeNode(postorder[post_index[0]])
#         post_index[0] -= 1
#
#         if start == end:
#             return new_node
#
#         index = inorder_hash[new_node.val]
#         new_node.right = build(index+1, end, inorder, postorder)
#         new_node.left = build(start, index-1, inorder, postorder)
#
#         return new_node
#
#     return build(0, len(inorder)-1, inorder, postorder)
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

from algorithms3.trees import build_tree_postorder
# root=build_tree_postorder.TreeNode(3)
# root.left=build_tree_postorder.TreeNode(9)
# root.right=build_tree_postorder.TreeNode(20)
#
# root.right.left=build_tree_postorder.TreeNode(15)
# root.right.right=build_tree_postorder.TreeNode(7)
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print2D(build_tree_postorder(inorder,postorder))