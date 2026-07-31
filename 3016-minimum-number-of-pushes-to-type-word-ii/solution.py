# Minimum Number of Pushes to Type Word II
# Difficulty: Medium
# Runtime: 414 ms
# Memory: 13 MB
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        # Count frequency of each character
        freq = Counter(word)

        # Sort frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)

        pushes = 0

        # Assign push cost
        for i, f in enumerate(frequencies):
            cost = (i // 8) + 1
            pushes += f * cost

        return pushes
