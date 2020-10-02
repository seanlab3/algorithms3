'''
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first 
number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number 
and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single 
number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
'''

# def elimination_game(A):
#     head = step = left = 1
#     while A > 1:
#         if left or A % 2 == 1:
#             head += step
#         A //= 2
#         step *= 2
#         left = 0 if left else 1
#
#     return head
from algorithms3.math import elimination_game
print(elimination_game(9))

