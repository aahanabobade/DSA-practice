# Count and Say
# Difficulty: Medium
# Runtime: 7 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/count-and-say/

                    count += 1
                else:
                    current += str(count) + result[i - 1]
                    count = 1
            
            # handle last group
            current += str(count) + result[-1]
            
            result = current
        
        return result
