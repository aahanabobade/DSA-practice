# Find Servers That Handled Most Number of Requests
# Difficulty: Hard
# Runtime: 3863 ms
# Memory: 32.7 MB
# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/


            if server == -1:
                server = find(1, 0, k - 1, 0)

            if server == -1:
                continue

            count[server] += 1
            update(1, 0, k - 1, server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]

