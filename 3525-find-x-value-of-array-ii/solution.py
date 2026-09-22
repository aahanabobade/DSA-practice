# Find X Value of Array II
# Difficulty: Hard
# Runtime: 8745 ms
# Memory: 65.5 MB
# https://leetcode.com/problems/find-x-value-of-array-ii/

            for rem in range(k):
                if right_cnt[rem]:
                    new_rem = left_product * rem % k
                    result_cnt[new_rem] += right_cnt[rem]

            total_product = left_product * right_product % k

            return total_product, result_cnt

        ans = []

        for idx, val, start, x in queries:
            set_leaf(size + idx, val)

            p = (size + idx) // 2
            while p:
                pull(p)
                p //= 2

            _, counts = query(start, n)
            ans.append(counts[x])

        return ans
