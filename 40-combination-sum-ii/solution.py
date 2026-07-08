# Combination Sum II
# Difficulty: Medium
# Runtime: 3 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/combination-sum-ii/


            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i], path)
                return
                ans.append(path[:])
            if remain == 0:
        def backtrack(start, remain, path):

        ans = []
