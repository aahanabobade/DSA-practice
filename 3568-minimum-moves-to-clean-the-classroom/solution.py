# Minimum Moves to Clean the Classroom
# Difficulty: Medium
# Runtime: 3025 ms
# Memory: 17.6 MB
# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

                if classroom[nr][nc] == 'X':
                    continue
                if e == 0:
                    continue

                ne = e - 1
                if classroom[nr][nc] == 'R':
                    ne = energy

                new_mask = mask
                if classroom[nr][nc] == 'L':
                    new_mask |= 1 << litter_id[(nr, nc)]

                if ne > visited[nr][nc][new_mask]:
                    visited[nr][nc][new_mask] = ne
                    q.append((nr, nc, ne, new_mask, dist + 1))

        return -1
