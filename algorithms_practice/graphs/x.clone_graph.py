'''
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. 
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},
{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as 
neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
'''

# class Node:
#     def __init__(self, val, neighbors):
#         self.val = val
#         self.neighbors = neighbors
#
# def cloneGraph(node):
#     copies = {}
#
#     def createCopy(node, copies):
#         newcopy = Node(node.val, None)
#         copies[node] = newcopy
#         nbors = []
#
#         if node.neighbors:
#             for item in node.neighbors:
#                 if item in copies:
#                     nbors.append(copies[item])
#                 else:
#                     nbors.append(createCopy(item, copies) )
#
#         newcopy.neighbors = nbors
#         return newcopy
#
#     return createCopy(node, copies)
#https://leetcode.com/problems/clone-graph/  leetcode 133

"""
bfs

from collections import defaultdict

class Solution(object):
    def cloneGraph(self, node):
     
    if not node:
        return None
    
    d = defaultdict(Node)
    queue = [node]
    d[node] = Node(node.val)

while queue:
    curr = queue.pop(0)
    for n in curr.neighbors:
        if n not in d:
            d[n] = Node(n.val)
            queue.append(n)
        d[curr].neighbors.append(d[n])
    return d[node]
####
dfs

from collections import defaultdict

class Solution(object):
    def dfs(self, node, d):
        if node in d:
            return
        d[node] = Node(node.val)
        for n in node.neighbors:
            if n not in d:
                self.dfs(n, d)
            d[node].neighbors.append(d[n])

    def cloneGraph(self, node):




if not node:
    return None

    d = defaultdict(Node)
    self.dfs(node, d)
    return d[node]



"""
### XXX
from algorithms3.graphs import clone_graph

adjList = [[2,4],[1,3],[2,4],[1,3]]

print(clone_graph.cloneGraph(adjList))

