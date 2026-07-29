# Smallest Palindromic Rearrangement II
# Difficulty: Hard
# Runtime: 954 ms
# Memory: 12.8 MB
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

                half[c] -= 1
                w = ways(half)
                if w >= k:
                    res.append(c)
                    m -= 1
                    break
                else:
                    k -= w
                    half[c] += 1

        first = "".join(res)
        return first + mid + first[::-1]
