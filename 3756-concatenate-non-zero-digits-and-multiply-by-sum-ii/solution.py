# Concatenate Non-Zero Digits and Multiply by Sum II
# Difficulty: Medium
# Runtime: 754 ms
# Memory: 52.4 MB
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

            left = cnt[l - 1] if l > 0 else 0
            right = cnt[r]

            if left == right:
                ans.append(0)
                continue

            digitSum = prefSum[right] - prefSum[left]

            x = (prefVal[right] - prefVal[left] * pow10[right - left]) % MOD

            ans.append((x * digitSum) % MOD)

        return ans
