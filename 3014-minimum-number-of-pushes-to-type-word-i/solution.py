# Minimum Number of Pushes to Type Word I
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        ans = 0

        for i in range(n):
            ans += (i // 8) + 1

        return ans
