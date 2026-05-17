# Jump Game III
# Difficulty: Medium
# Runtime: 39 ms
# Memory: 71.3 MB
# https://leetcode.com/problems/jump-game-iii/

                return True

            visited.add(i)

            # try both directions
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)
