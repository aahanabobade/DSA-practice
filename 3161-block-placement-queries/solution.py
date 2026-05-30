# Block Placement Queries
# Difficulty: Hard
# Runtime: 7922 ms
# Memory: 69.9 MB
# https://leetcode.com/problems/block-placement-queries/

                results.append(best >= sz)

        results.reverse()
        return results
                if prev > 0:
                    best = max(best, query(prev))
                obstacles.remove(x)
            else:
                x, sz = q[1], q[2]
                # bisect_left: find obstacle strictly before x
                idx = obstacles.bisect_left(x) - 1
                prev = obstacles[idx]
                best = x - prev
