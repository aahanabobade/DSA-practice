# Find the Prefix Common Array of Two Arrays
# Difficulty: Medium
# Runtime: 22 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])
            
            result.append(len(setA & setB))
        
        return result
        
