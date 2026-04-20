# Two Furthest Houses With Different Colors
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

                break
            
        for i in range(n):
            if colors[i]!=colors[n-1]:
                dist=max(dist,n-1-i)
                break
        
        return dist

