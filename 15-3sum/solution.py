# 3Sum
# Difficulty: Medium
# Runtime: 823 ms
# Memory: 18.8 MB
# https://leetcode.com/problems/3sum/


                if total ==0:
                    ans.append([nums[i],nums[left],nums[right]])

                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left - 1]:
                        left+=1
                total = nums[i]+nums[left]+nums[right]
            while left<right:

                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                
                elif total <0:
                    left+=1
                
                elif total>0:
                    right-=1
        
        return ans
