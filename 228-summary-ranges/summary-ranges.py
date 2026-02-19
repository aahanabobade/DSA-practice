class Solution(object):
    def summaryRanges(self, nums):
        result = []
        n = len(nums)

        if n == 0:
            return result

        start = nums[0]

        for i in range(n):
            # if end of range
            if i == n - 1 or nums[i] + 1 != nums[i + 1]:
                end = nums[i]

                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))

                # start new range
                if i + 1 < n:
                    start = nums[i + 1]

        return result
