
class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        target = sorted(nums)

        def check(k):
            for start in range(0, n, k):
                end = start + k

                if sorted(nums[start:end]) != target[start:end]:
                    return False

                drops = 0
                for i in range(start, end - 1):
                    if nums[i] > nums[i + 1]:
                        drops += 1

                if nums[end - 1] > nums[start]:
                    drops += 1

                if drops > 1:
                    return False

            return True

        ans = 0
        for k in range(1, n + 1):
            if n % k == 0 and check(k):
                ans += k

        return ans
