# Maximum Product Subarray
# Difficulty: Medium
# Runtime: 13 ms
# Memory: 13.2 MB
# https://leetcode.com/problems/maximum-product-subarray/

                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            result = max(result, max_prod)

        return result
