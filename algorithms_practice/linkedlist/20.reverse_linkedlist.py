'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# def reverse_list_iterative(head):
#     prev, current, next = None, head, None
#     while current:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#     return prev
#
# def reverse_list_recursive(head):
#     head = [head]
#     def helper(current, prev):
#         if current.next is None:
#             head[0] = current
#             current.next = prev
#             return
#         next = current.next
#         current.next = prev
#         helper(next, current)
#
#     if head[0] is None:
#         return None
#
#     helper(head[0], None)
#     return head[0]
#
# def reverse_list_v2(head):
#     def helper(current, prev):
#         if current.next is None:
#             current.next = prev
#             return current
#         next = current.next
#         current.next = prev
#         new_node = helper(next, current)
#         return new_node
#
#     if head is None:
#         return
#     return helper(head, None)
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
from algorithms3.linkedlist import reverse_linkedlist
a=makeLinkedNode([1,2,3,4,5])
aa=makeLinkedNode([1,2,3,4,5])
aaa=makeLinkedNode([1,2,3,4,5])

b=reverse_linkedlist.reverse_list_iterative(a)
printList(b)

c=reverse_linkedlist.reverse_list_recursive(aa)
printList(c)


d=reverse_linkedlist.reverse_list_v2(aaa)
printList(d)











































