'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

# def delete_duplicates(head):
#     current = head
#     while current:
#         prev = current
#         while prev.next and prev.val == prev.next.val:
#             prev = prev.next
#         current.next = prev.next
#         current = current.next
#     return head

class Node:
    def __init__(self, x, nextNode = None):
        self.val = x
        self.next = nextNode
def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))

#11233
from algorithms3.linkedlist import delete_duplicates
root=Node(1)
l2=Node(1,root)
l3=Node(2,l2)
l4=Node(3,l3)
l5=Node(3,l4)
printList(l5)

l6=delete_duplicates(l5)
printList(l6)

