# 3Sum
# Difficulty: Medium
# Runtime: 768 ms
# Memory: 18.3 MB
# https://leetcode.com/problems/3sum/

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # skip duplicates for left
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    # skip duplicates for right
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
