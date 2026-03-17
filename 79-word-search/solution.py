# Word Search
# Difficulty: Medium
# Runtime: 5718 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/word-search/

                return False

            temp = board[i][j]
            board[i][j] = "#"

            # explore 4 directions
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:

                return True
            if k == len(word):
            # k = index in word
        def dfs(i, j, k):
