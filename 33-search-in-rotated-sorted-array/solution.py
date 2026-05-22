# Search in Rotated Sorted Array
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/search-in-rotated-sorted-array/

                return mid
            
            if nums[left]<=nums[mid]:
                if nums[left]<=target <=nums[mid]:
                    right = mid -1
                else:
                    left = mid+1

            else:
                if nums[mid] <target <=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
                    
        return -1
