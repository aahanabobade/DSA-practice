# Merge Sorted Array
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/merge-sorted-array/

        p=m+n-1
        while p1>= 0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[p]=nums1[p1]
                p1-=1
            else:
                nums1[p]=nums2[p2]
                p2-=1
            p-=1

        while p2>=0:
            nums1[p]=nums2[p2]
            p2-=1
            p-=1
