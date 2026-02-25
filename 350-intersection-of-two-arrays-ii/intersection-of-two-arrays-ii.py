class Solution(object):
    def intersect(self, nums1, nums2):
        final = []

        for num in nums1:
            if num in nums2:
                final.append(num)
                nums2.remove(num)

        return final