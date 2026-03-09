# Relative Ranks
# Difficulty: Easy
# Runtime: 1942 ms
# Memory: 13 MB
# https://leetcode.com/problems/relative-ranks/

                result[max_index] = "Silver Medal"
            elif rank == 3:
                result[max_index] = "Bronze Medal"
            else:
                result[max_index] = str(rank)
            
            score[max_index] = -1
        
        return result
