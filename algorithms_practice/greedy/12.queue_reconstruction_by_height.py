'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of 
integers (h, k), where h is the height of the person and k is the number of people in front of this person 
who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

# from collections import deque
#
# def reconstruct_queue(people):
#     order = deque()
#     people.sort(key = lambda x: (-x[0], x[1]))
#     for pair in people:
#         order.insert(pair[1], pair)
#
#     return list(order)
from algorithms3.greedy import queue_reconstruction_by_height
a=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(queue_reconstruction_by_height.reconstruct_queue(a))


