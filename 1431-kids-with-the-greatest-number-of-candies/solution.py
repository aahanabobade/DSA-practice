# Kids With the Greatest Number of Candies
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

        :type extraCandies: int
        :rtype: List[bool]
        """
        maxx = max(candies)

        n = len(candies)
        for i in range(n):
        result = []
            if candies[i]+extraCandies>=maxx:
                result.append(True)
            else:
                result.append(False)
        
        return result
