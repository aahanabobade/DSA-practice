# Maximum Number of Balloons
# Difficulty: Easy
# Runtime: 8 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/maximum-number-of-balloons/


        for i in text:
            count[i] = count.get(i, 0) + 1

        return min(
            count.get('b', 0),
            count.get('a', 0),
            count.get('l', 0) // 2,
            count.get('o', 0) // 2,
            count.get('n', 0)
        )
