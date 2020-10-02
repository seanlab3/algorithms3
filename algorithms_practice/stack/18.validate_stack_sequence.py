'''
Given two sequences pushed and popped with distinct values, return true if and only if this could 
have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
'''

# def validate_stack(pushed, popped):
#     stack = []
#     popped = popped[::-1]
#
#     for val in pushed:
#         stack.append(char)
#         while stack and popped and stack[-1] == popped[-1]:
#             stack.pop()
#             popped.pop()
#
#     return len(stack) == 0
from algorithms3.stack import validate_stack_sequence
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

print(validate_stack_sequence.validate_stack(pushed,popped))