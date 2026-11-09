
class Solution(object):
    def busiestServers(self, k, arrival, load):
        import heapq

        tree = [0] * (4 * k)

        def build(node, left, right):
            if left == right:
                tree[node] = 1
                return

            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def update(node, left, right, pos, val):
            if left == right:
                tree[node] = val
                return

            mid = (left + right) // 2

            if pos <= mid:
                update(node * 2, left, mid, pos, val)
            else:
                update(node * 2 + 1, mid + 1, right, pos, val)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def find(node, left, right, start):
            if tree[node] == 0 or right < start:
                return -1

            if left == right:
                return left

            mid = (left + right) // 2

            ans = find(node * 2, left, mid, start)

            if ans != -1:
                return ans

            return find(node * 2 + 1, mid + 1, right, start)

        build(1, 0, k - 1)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(1, 0, k - 1, server, 1)

            server = find(1, 0, k - 1, i % k)

            if server == -1:
                server = find(1, 0, k - 1, 0)

            if server == -1:
                continue

            count[server] += 1
            update(1, 0, k - 1, server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
