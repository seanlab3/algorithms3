'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# def reorder_list(head):
#     if not head or not head.next:
#         return head
#
#     slow = fast = head
#
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#
#     current = slow.next
#     node = slow.next = None
#
#     while current:
#         current.next, node, current = node, current, current.next
#
#     cur1, cur2 = head, node
#     while cur2: # insert
#         next1, next2 = cur1.next, cur2.next
#         cur1.next, cur2.next = cur2, next1
#         cur1, cur2 = next1, next2
#     return head
class ListNodeSort:
    def __init__(self, x):
        self.val = x
        self.next = None
def makeLinkedNode(alist):

    nodelist=[ListNodeSort(i) for i in alist]
    for i in range(len(alist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0]
def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))

from algorithms3.linkedlist import reorder_list

a=makeLinkedNode([1,2,3,4])
b=reorder_list(a)
printList(b)