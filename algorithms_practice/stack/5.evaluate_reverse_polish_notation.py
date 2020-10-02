'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another 
expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would 
always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

# def eval_rpn(tokens):
#     stack = []
#     operators = {'+':(lambda x,y: x+y), '-':(lambda x,y: x-y),
#                  '*':(lambda x,y: x*y), '/':(lambda x,y: x/y)}
#
#     for token in tokens:
#         if token in operators:
#             number2 = stack.pop()
#             number1 = stack.pop()
#             stack.append(operators[token](int(number1), int(number2)))
#         else:
#             stack.append(token)
#
#     return int(stack.pop())
from algorithms3.stack import evaluate_reverse_polish_notation

a=["2", "1", "+", "3", "*"]
print(evaluate_reverse_polish_notation.eval_rpn(a))