# Minimum Number of Flips to Make the Binary String Alternating
# Difficulty: Medium
# Runtime: 743 ms
# Memory: 21.2 MB
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

        for i in range(2 * n):
            if s[i] != pattern1[i]:
                flips1 += 1
            if s[i] != pattern2[i]:
                flips2 += 1

            if i >= n:
                if s[i - n] != pattern1[i - n]:
                    flips1 -= 1
                if s[i - n] != pattern2[i - n]:
                    flips2 -= 1

