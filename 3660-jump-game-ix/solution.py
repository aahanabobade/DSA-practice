# Jump Game IX
# Difficulty: Medium
# Runtime: 240 ms
# Memory: 41.1 MB
# https://leetcode.com/problems/jump-game-ix/


        for i in range(len(stack)):
            for j in range(stack[i][1], stack[i][2] + 1):
                ans[j] = stack[i][0]

        return ans
