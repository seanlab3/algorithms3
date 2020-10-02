'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


# def reverse_mn(head, m, n):
#     if head is None:
#         return None
#
#     prev, current = None, head
#
#     while m > 1:
#         prev = current
#         current = current.next
#         m -= 1
#         n -= 1
#
#     temp = prev
#     tail = current
#     while n > 0:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#         n -= 1
#
#     if temp: temp.next = prev
#     else: head = prev
#     tail.next = current
#
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

from algorithms3.linkedlist import reverse_mn
a=makeLinkedNode([1,2,3,4,5])
m=2
n=4
b=reverse_mn(a,m,n)
printList(b)