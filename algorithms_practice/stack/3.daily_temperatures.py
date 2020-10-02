'''
Given a list of daily temperatures T, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. If there is no 
future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output 
should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an 
integer in the range [30, 100].
'''

# def daily_temperatures(T):
#     stack, result = [], [0] * len(T)
#     for index, temp in enumerate(T):
#         while stack and stack[-1][1] < temp:
#             result[stack[-1][0]] = index - stack[-1][0]
#             stack.pop()
#         stack.append([index, temp])
#
#     return result
from algorithms3.stack import daily_temperatures

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(T))

