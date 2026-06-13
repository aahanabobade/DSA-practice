# Weighted Word Mapping
# Difficulty: Easy
# Runtime: 20 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/weighted-word-mapping/

        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans = []

        for i in words:
            total = 0
            for ch in i:
                total += weights[ord(ch) - ord('a')]

            rem = total % 26
            ans.append(chr(ord('z') - rem))

        return "".join(ans)
