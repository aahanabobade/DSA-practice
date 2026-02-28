class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        # Mark indices corresponding to numbers present
        for i in range(n):
            value = nums[i]
            if value < 0:
                value = -value  

            index = value - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []

        # Indices that remain positive are missing numbers
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result