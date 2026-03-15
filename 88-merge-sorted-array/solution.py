# Merge Sorted Array
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/merge-sorted-array/

                nums1[k] = nums2[j]
            else:
                nums1[k] = nums1[i]
                i -= 1
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
