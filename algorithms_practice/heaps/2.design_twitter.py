'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''

# import heapq
# from collections import defaultdict
#
# class Twitter:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.users = defaultdict(list)
#         self.followed = defaultdict(set)
#
#     def add_tweet(self, userId, tweetId):
#         if not self.users[userId]:
#             self.users[userId].append((1, tweetId))
#         else:
#             heapq.heappush(self.users[userId], (self.users[userId][-1][0] + 1, tweetId))
#         if len(self.users[userId]) > 10: heapq.heappop(self.users[userId])
#
#     def postTweet(self, userId: int, tweetId: int) -> None:
#         """
#         Compose a new tweet.
#         """
#
#         self.add_tweet(userId, tweetId)
#         for follower in self.followed[userId]:
#             self.add_tweet(follower, tweetId)
#
#     def getNewsFeed(self, userId: int):
#         """
#         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
#         """
#         return self.users[userId]
#
#     def follow(self, followerId: int, followeeId: int) -> None:
#         """
#         Follower follows a followee. If the operation is invalid, it should be a no-op.
#         """
#         self.followed[followeeId].add(followerId)
#
#
#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         """
#         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
#         """
#         self.followed[followeeId].remove(followerId)
from algorithms3.heaps import design_twitter

twitter = design_twitter.Twitter()
# User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5)

# User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1)

# User 1 follows user 2.
twitter.follow(1, 2)

# User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6)

# User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1)

# User 1 unfollows user 2.
twitter.unfollow(1, 2)

# User 1's news feed should return a list with 1 tweet id -> [5],
# since user 1 is no longer following user 2.
twitter.getNewsFeed(1)



