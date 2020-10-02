'''
The demons had captured the princess (P) and imprisoned her in the bottom-
right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 
2D grid. Our valiant knight (K) was initially positioned in the top-left room 
and must fight his way through the dungeon to rescue the princess. The knight 
has an initial health point represented by a positive integer. If at any point 
his health point drops to 0 or below, he dies immediately. Some of the rooms 
are guarded by demons, so the knight loses health (negative integers) upon 
entering these rooms; other rooms are either empty (0's) or contain 
magic orbs that increase the knight's health (positive integers). In order
to reach the princess as quickly as possible, the knight decides to move only 
rightward or downward in each step. Write a function to determine the knight's 
minimum initial health so that he is able to rescue the princess. For example, 
given the dungeon below, the initial health of the knight must be at least 7 if 
he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN. Dungeon 
Princess: Example 1 
Input arguments to function: Your function will get an M*N matrix (2-D array) 
as input which represents the 2D grid as described in the question. Your 
function should return an integer corresponding to the knight's minimum 
initial health required.

 Note:
The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight 
enters and the bottom-right room where the princess is imprisoned.
'''

# def calculateMinimumHP(A):
#     A[-1][-1] = max(1, 1 - A[-1][-1])
#
#     for i in range(len(A) - 2, -1, -1):
#         A[i][-1] = max(1, A[i + 1][-1] - A[i][-1])
#
#     for j in range(len(A[0]) - 2, -1, -1):
#         A[-1][j] = max(1, A[-1][j + 1] - A[-1][j])
#
#     for i in range(len(A) - 2, -1, -1):
#         for j in range(len(A[0]) - 2, -1, -1):
#             choice = min(A[i + 1][j], A[i][j + 1])
#             A[i][j] = max(1, choice - A[i][j])
#
#     return A[0][0]
#https://leetcode.com/problems/dungeon-game/


from algorithms3.dp import dungeon_princess

a=[[-2,-3,3],
   [-5,-10,1],
   [10,30,-5]
   ]
print(dungeon_princess.calculateMinimumHP(a))