'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
'''
# from collections import Counter
#
# def deck_cards(deck):
#     count = Counter(deck)
#     min_x = min(count.values())
#     if min_x < 2: return False
#     for rem in range(2, min_x + 1):
#         for val in count.values():
#             if val % rem: break
#         else:
#             return True
#
#     return False
from algorithms3.hashtables import deck_of_cards
a=[1,2,3,4,4,3,2,1]
print(deck_of_cards.deck_cards(a))