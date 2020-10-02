# def bubble_sort(nums:list) -> list:
#     '''
#     returns sorted list
#     Time Complexity: O(n^2)
#     Space Complexity: O(1)
#     '''
#     for i in range(len(nums) - 1):
#         swapped = False
#         for j in range(len(nums) - i - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#                 swapped = True
#
#         if not swapped: break
#
#     return nums
from algorithms3.sort import bubble_sort
import random
alist=[random.randrange(1,10) for i in range(10)]
print(alist)
print(bubble_sort(alist))




