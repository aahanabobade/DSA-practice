# Intersection of Two Arrays II
# Difficulty: Easy
# Runtime: 19 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/intersection-of-two-arrays-ii/


        for i in range(m):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])

        return res
        res = []
        m = len(nums1)
        """
        :rtype: List[int]
