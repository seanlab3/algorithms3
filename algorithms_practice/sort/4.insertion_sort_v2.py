# def insertion_sort(nums):
#     '''
#     returns sorted list
#     '''
#     for i in range(1, len(nums)):
#         value = nums[i]
#
#         for j in range(i - 1, -1, -1):
#             if nums[j] > value:
#                 nums[j + 1] = nums[j]
#             else: break
#
#         nums[j] = value
#
#     return nums
from algorithms3.sort import insertion_sort

import random
alist=[random.randrange(1,10) for i in range(10)]
print(alist)
print(insertion_sort(alist))