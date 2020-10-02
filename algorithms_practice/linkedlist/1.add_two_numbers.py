'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 
0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# from .singly_linked_list_implementation import *
#
# def add_two_numbers(l1, l2):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#     current = Node(0)
#     newNode = current
#     carry = 0
#     while l1 or l2:
#         first = l1.val if l1 else 0
#         second = l2.val if l2 else 0
#
#         sumx = first + second + carry
#         carry = sumx // 10
#         sumx %= 10
#
#         temp = Node(sumx)
#         newNode.next = temp
#         newNode = newNode.next
#         if l1: l1 = l1.next
#         if l2: l2 = l2.next
#
#     if carry:
#         temp = Node(carry)
#         newNode.next = temp
#
#     return current.next
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
from algorithms3.linkedlist import add_two_numbers,singly_linked_list_implementation

#789

root=Node(7)
l2=Node(8,root)
l3=Node(9,l2)

printList(l3)
#478

root2=Node(4)
l3=Node(7,root2)
l4=Node(8,l3)
printList(l4)

l5 = add_two_numbers.add_two_numbers_v2(l3, l4)
printList(l5)


l6 = add_two_numbers.add_two_numbers_v2(l3, l4)
printList(l6)
print()

############################













