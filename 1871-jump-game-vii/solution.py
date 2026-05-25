# Jump Game VII
# Difficulty: Medium
# Runtime: 271 ms
# Memory: 16 MB
# https://leetcode.com/problems/jump-game-vii/

            i = q.popleft()
            
        while q:
        
        farthest = 0
        # farthest index already scanned
        
        q = deque([0])
        n = len(s)
        
        """
        :rtype: bool
        :type maxJump: int
        :type s: str
        :type minJump: int
        """
