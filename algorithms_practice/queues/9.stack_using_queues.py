'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
'''

# from collections import deque
# class MyStack:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.que = deque()
#
#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.que.append(x)
#         for i in range(len(self.que)-1):
#             val = self.pop()
#             self.que.append(val)
#
#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         return self.que.popleft()
#
#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.que[0]
#
#
#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return True if len(self.que) == 0 else False
from algorithms3.queues import stack_using_queues

obj=stack_using_queues.MyStack()
obj.push(10)
obj.push(9)
obj.push(8)
print(obj.pop())
print(obj.top())