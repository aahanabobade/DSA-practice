class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        p = nums.index(0)

        inc = all(nums[(p + i) % n] == i for i in range(n))
        dec = all(nums[(p - i) % n] == i for i in range(n))

        ans = float('inf')

        if inc:
            ans = min(ans, p, n - p + 2)

        if dec:
            ans = min(ans, p + 2, n - p)

        return -1 if ans == float('inf') else ans
