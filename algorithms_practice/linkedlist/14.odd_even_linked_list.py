'''
Given a singly linked list, group all odd nodes together followed by 
the even nodes. Please note here we are talking about the node number and 
not the value in the nodes.

You should try to do it in place. The program should run in O(1) space 
complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain 
as it was in the input.
The first node is considered odd, the second node even and so on ...
'''
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
# def odd_even_list(head):
#     if not head: return head
#     odd, even = head, head.next
#     even_head = head.next
#
#     while even and even.next:
#         odd.next = odd.next.next
#         odd = odd.next
#         even.next = even.next.next
#         even = even.next
#
#     odd.next = even_head
#     return head
from algorithms3.linkedlist import odd_even_linked_list

a=makeLinkedNode([2,1,3,5,6,4,7,"NULL"])

b=odd_even_linked_list.odd_even_list(a)
printList(b)



    