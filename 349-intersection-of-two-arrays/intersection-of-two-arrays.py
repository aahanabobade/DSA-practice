class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        n =len(nums1)
        m = len(nums2)
        res = set()
        inter = set()

        for i in range(n):
            res.add(nums1[i])

        for j in range(m):
            if nums2[j] in res:
                inter.add(nums2[j])
        
        return list(inter)