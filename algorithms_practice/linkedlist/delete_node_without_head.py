'''
Write a function to delete a node (except the tail) in a singly linked list, 
given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 
4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 
4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
'''

# def delete_node_value(node):
#     node.val = node.next.val
#     node.next = node.next.nex
#
# def delete_node_value_v2(node):
#     prev, current = node, node.next
#     while current.next:
#         prev.val = current.val
#         prev = current
#         current = current.next
#
#     prev.val = current.val
#     prev.next = None
class ListNodeSort:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))

#4->5->1->9
from algorithms3.linkedlist import delete_node_without_head

node=ListNodeSort(4)
node1=ListNodeSort(5)
node.next=node1
node2=ListNodeSort(1)
node1.next=node2
node3=ListNodeSort(9)
node2.next=node3
printList(node)
deletenoe=ListNodeSort(1)
result=delete_node_without_head.delete_node_value(deletenoe)
printList(result)

c=delete_node_without_head.delete_node_value(b)
c.printList()



