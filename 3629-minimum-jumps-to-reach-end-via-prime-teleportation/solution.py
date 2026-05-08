# Minimum Jumps to Reach End via Prime Teleportation
# Difficulty: Medium
# Runtime: 677 ms
# Memory: 147.6 MB
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

                if len(factors[nums[i]]) == 1:
                    p = nums[i]
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1
