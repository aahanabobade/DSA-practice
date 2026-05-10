# Intersection of Two Arrays II
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/intersection-of-two-arrays-ii/


        for i in nums1:
            freq[i] = freq.get(i, 0) + 1

        # check nums2
        for i in nums2:
        result = []
            if i in freq and freq[i] > 0:
                result.append(i)
                freq[i] -= 1

        return result
        freq = {}
        """
        :rtype: List[int]
