'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

# def rotate_list(head, k):
#     if not head or k == 0 or not head.next:
#             return head
#     count = 0
#     current = head
#     while current:
#         current = current.next
#         count += 1
#     k %= count
#     if k == 0: return head
#
#     prev, current = None, head
#     while count - k > 0:
#         prev = current
#         current = current.next
#         count -= 1
#
#     prev.next = None
#     new_head = current
#
#     while current.next:
#         current = current.next
#
#     current.next = head
#
#     return new_head
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
from algorithms3.linkedlist import rotate_list

a=makeLinkedNode([1,2,3,4,5])
k=2
b=rotate_list(a,k)
printList(b)
