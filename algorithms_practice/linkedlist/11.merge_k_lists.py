'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe 
its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# from .singly_linked_list_implementation import Node as ListNode
# import heapq
# import itertools

# def merge_k_lists(lists) -> ListNode:
#     '''
#     @param1: a list of the heads of the k linked lists
#     @return: head of merged list
#     '''
#     minheap = []
#     head = current = ListNode(0)
#     counter = itertools.count()
#     for node in lists:
#         if node:
#             heapq.heappush(minheap, (node.val, next(counter), node))
#     while len(minheap) > 0:
#         val, tie, node = heapq.heappop(minheap)
#         current.next = ListNode(val)
#         current = current.next
#         node = node.next
#         if node:
#             heapq.heappush(minheap, (node.val, next(counter), node))
#     return head.next
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
from algorithms3.linkedlist import merge_k_lists


a=makeLinkedNode([1,4,5])
b=makeLinkedNode([1,3,4])
c=makeLinkedNode([2,6])
b=merge_k_lists([a,b,c])
printList(b)


