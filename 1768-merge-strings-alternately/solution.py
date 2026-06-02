# Merge Strings Alternately
# Difficulty: Easy
# Runtime: 19 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/merge-strings-alternately/


        while i < m and j<n:
            result.append(word2[j])
            i+=1
            j+=1
        
        result.append(word1[i:])
        result.append(word2[j:])

            result.append(word1[i])
        return "".join(result)
