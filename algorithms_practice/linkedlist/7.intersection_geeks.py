# class Node:
#     def __init__(self):
#         self.data = 0
#         self.next = None
#
# # Function to get the intersection point
# # of the given linked lists
# def getIntersectionNode( head1, head2):
#
#     curr1 = head1
#     curr2 = head2
#
#     # While both the pointers are not equal
#     while (curr1 != curr2):
#
#         # If the first pointer is None then
#         # set it to point to the head of
#         # the second linked list
#         if (curr1 == None) :
#             curr1 = head2
#
#             # Else point it to the next node
#         else:
#             curr1 = curr1.next
#
#         # If the second pointer is None then
#         # set it to point to the head of
#         # the first linked list
#         if (curr2 == None):
#             curr2 = head1
#
#             # Else point it to the next node
#         else:
#             curr2 = curr2.next
#
#     # Return the intersection node
#     return curr1.data

# 1st Linked list is 3.6.9.15.30
# 2nd Linked list is 10.15.30

# 15 is the intersection point

class ListNodeSort:
    def __init__(self):
        self.val = 0
        self.next = None




def printList(l):
    value = []
    while(l):
        value.append(l.val)
        l = l.next
    print(' -> '.join(map(str, value)))
from algorithms3.linkedlist import intersection_geeks

# 10 3 6 9 15 30
newNode = None
head1 = intersection_geeks.Node()
head1.data = 10
head2 = intersection_geeks.Node()
head2.data = 3
newNode = intersection_geeks.Node()
newNode.data = 6
head2.next = newNode
newNode = intersection_geeks.Node()
newNode.data = 9
head2.next.next = newNode
newNode = intersection_geeks.Node()
newNode.data = 15
head1.next = newNode
head2.next.next.next = newNode
newNode = intersection_geeks.Node()
newNode.data = 30


head1.next.next = newNode
head1.next.next.next = None
print( intersection_geeks.getIntersectionNode(head1, head2))





