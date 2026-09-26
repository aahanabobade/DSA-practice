# Evaluate the Bracket Pairs of a String
# Difficulty: Medium
# Runtime: 67 ms
# Memory: 56.1 MB
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

                ans.append(mp.get(key, '?'))

                i = j + 1
            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)

