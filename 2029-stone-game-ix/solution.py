# Stone Game IX
# Difficulty: Medium
# Runtime: 59 ms
# Memory: 20.3 MB
# https://leetcode.com/problems/stone-game-ix/

        cnt = [0, 0, 0]

        for stone in stones:
            cnt[stone % 3] += 1

        c0, c1, c2 = cnt

        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0

        return abs(c1 - c2) > 2
        """
        :type stones: List[int]
        :rtype: bool
        """
