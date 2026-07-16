# Sum of GCD of Formed Pairs
# Difficulty: Medium
# Runtime: 771 ms
# Memory: 22.4 MB
# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

        total = 0
        i, j = 0, n - 1
        while i < j:
            total += gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1
        
        return total
