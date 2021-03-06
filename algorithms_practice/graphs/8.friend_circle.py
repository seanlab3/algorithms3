'''
There are N students in a class. Some of them are friends, while some are not. 
Their friendship is transitive in nature. For example, if A is a direct friend of B, and B
 is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle 
 is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If 
M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, 
so return 1.
'''

# from collections import deque
#
# def friend_circle(M):
#
#     def bfs(index):
#         que = deque([index])
#
#         while que:
#             current = que.popleft()
#             visited.add(current)
#
#             for index, vertex in enumerate(M[current]):
#                 if index not in visited and vertex != 0:
#                     que.append(index)
#                     visited.add(index)
#     count = 0
#     visited = set()
#     for index in range(len(M)):
#         if index not in visited:
#             count += 1
#             bfs(index)
#
#     return count
#
# def friend_circle_v2(M):
#
#     def dfs(index):
#         visited.add(index)
#
#         for index, vertex in enumerate(M[index]):
#             if index not in visited and vertex != 0:
#                 dfs(index)
#
#     count = 0
#     visited = set()
#     for index in range(len(M)):
#         if index not in visited:
#             count += 1
#             dfs(index)
#
#     return count
from algorithms3.graphs import friend_circle
a=[[1,1,0],
   [1,1,0],
   [0,0,1]]
print(friend_circle.friend_circle_v1(a))

print(friend_circle.friend_circle_v2(a))