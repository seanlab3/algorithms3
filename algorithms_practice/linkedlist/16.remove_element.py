'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# def remove_elements(head, val):
#     while head and head.val == val:
#         head = head.next
#
#     if not head: return
#     prev, current = head, head.next
#
#
#     while current:
#         if current.val == val:
#             prev.next = current.next
#             current = current.next
#         else:
#             prev = current
#             current = current.next
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

from algorithms3.linkedlist import remove_element

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
a=makeLinkedNode([1,2,6,3,4,5,6])
val=6
b=remove_element.remove_elements(a,val)
printList(b)