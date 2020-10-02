'''Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string 
inside the square brackets is being repeated exactly k times. Note 
that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white 
spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any 
digits and that digits are only for those repeat numbers, k. For example, 
there won't be input like 3a or 2[4].

''인코딩 된 문자열을주고, 디코딩 된 문자열을 반환합니다.

인코딩 규칙은 k [encoded_string]입니다. 여기서 encoding_string
대괄호 안에 정확히 k 번 반복됩니다. 노트
k는 양의 정수임을 보증합니다.

입력 문자열이 항상 유효하다고 가정 할 수 있습니다. 여분의 흰색 없음
공백, 대괄호 등이 잘 구성되어 있습니다.

또한 원본 데이터에 포함되지 않은 것으로 가정 할 수 있습니다
자릿수와 그 자릿수는 반복되는 숫자 k에만 해당됩니다. 예를 들어
3a 또는 2 [4]와 같은 입력은 없습니다.
'''

# from collections import deque
# def decode_string(s):
#     stack = []
#
#     i = 0
#     while i < len(s):
#         while i < len(s) and s[i] != ']':
#             stack.append(s[i])
#             i += 1
#
#         if i == len(s): break
#         i += 1
#         string = deque()
#         while stack and stack[-1] != '[':
#             string.insert(0, stack.pop())
#
#         stack.pop()
#         num = deque()
#         while stack and stack[-1].isdigit():
#             num.insert(0, stack.pop())
#         num = int(''.join(num))
#
#         result = num * ''.join(string)
#         stack.append(result)
#
#     return ''.join(stack)
from algorithms3.strings import decode_string
a=["a","a","a"]
print(decode_string(a))






