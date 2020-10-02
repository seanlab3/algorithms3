'''
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# def delete_all_duplicates(head):
#     dummy = pre = ListNode(0)
#     dummy.next = head
#     while head and head.next:
#         if head.val == head.next.val:
#             while head and head.next and head.val == head.next.val:
#                 head = head.next
#             head = head.next
#             pre.next = head
#         else:
#             pre = pre.next
#             head = head.next
#     return dummy.next
from algorithms3.linkedlist import delete_duplicates_all
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))

#1->2->3->3->4->4->5

result = ListNode(1)
result_tail = result
result_tail.next = ListNode(2)
result_tail = result_tail.next
result_tail.next = ListNode(3)
result_tail = result_tail.next
result_tail.next = ListNode(3)

result_tail = result_tail.next
result_tail.next = ListNode(4)
result_tail = result_tail.next
result_tail.next = ListNode(4)

result_tail = result_tail.next
result_tail.next = ListNode(5)
printList(result)
from algorithms3.linkedlist import delete_duplicates_all

a=delete_duplicates_all.delete_all_duplicates(result)
printList(a)