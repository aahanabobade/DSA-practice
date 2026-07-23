# Number of Unique XOR Triplets I
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 21.3 MB
# https://leetcode.com/problems/number-of-unique-xor-triplets-i/

    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # For n = 1 or 2, only the numbers themselves are possible
        if n < 3:
            return n

        # Smallest power of 2 strictly greater than n
        return 1 << n.bit_length()
