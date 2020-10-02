'''
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

 

Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
 

Note:

Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.
'''
# from collections import deque
#
# class RecentCounter:
#
#     def __init__(self):
#         self.time = deque()
#
#     def ping(self, t: int) -> int:
#         self.time.append(t)
#         while self.time[0] < t - 3000:
#             self.time.popleft()
#         return len(self.time)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
from algorithms3.math import total_time

inputs1 = ["RecentCounter","ping","ping","ping","ping"]

inputs2 = [[],[1],[100],[3001],[3002]]

obj = total_time.RecentCounter()
param_1 = obj.ping(inputs2)

print(param_1)