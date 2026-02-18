class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        freq = {}

        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        for i in range(n):
            for j in range(0, n - i - 1):
                
                if (freq[nums[j]] > freq[nums[j+1]]) or \
                   (freq[nums[j]] == freq[nums[j+1]] and nums[j] < nums[j+1]):
                    
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums
