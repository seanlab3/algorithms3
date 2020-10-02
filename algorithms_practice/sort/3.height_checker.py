'''
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  
(This is the number of students that must move in order for all students to be standing 
in non-decreasing order of height.)

 

Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.
 

Note:

1 <= heights.length <= 100
1 <= heights[i] <= 100
'''

# def height_checker(heights):
#     count = 0
#     sorted_heights = sorted(heights)
#     for i in range(len(heights)):
#         if sorted_heights[i] != heights[i]:
#             count += 1
#
#     return count
from algorithms3.sort import height_checker
a=[1,1,4,2,1,3]
print(height_checker(a))
