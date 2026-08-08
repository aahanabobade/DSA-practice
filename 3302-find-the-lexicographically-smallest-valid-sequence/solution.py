# Find the Lexicographically Smallest Valid Sequence
# Difficulty: Medium
# Runtime: 705 ms
# Memory: 49.5 MB
# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

            elif not used_mismatch:
                # We need all remaining characters word2[j+1:]
                # to be matchable after i.
                if j == m - 1 or (suf[j + 1] != -1 and suf[j + 1] > i):
                    ans.append(i)
                    used_mismatch = True
                    i += 1
                    j += 1
                else:
                    i += 1

            else:
                i += 1

        if j == m:
            return ans

        return []
