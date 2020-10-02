'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes 
greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# def partition_list(head, x):
#     before = before_head = ListNode(0)
#     after = after_head = ListNode(0)
#
#     while head:
#         if head.val < x:
#             before.next = head
#             before = before.next
#         else:
#             after.next = head
#             after = after.next
#         head = head.next
#
#     after.next = None
#     before.next = after_head.next
#
#     return before_head.next
#
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

from algorithms3.linkedlist import partition_list

#1->4->3->2->5->2, x = 3
x=3
a=makeLinkedNode([1,4,3,2,5,2])
b=partition_list(a,x)
printList(b)