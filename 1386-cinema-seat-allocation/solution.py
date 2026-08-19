# Cinema Seat Allocation
# Difficulty: Medium
# Runtime: 143 ms
# Memory: 17.4 MB
# https://leetcode.com/problems/cinema-seat-allocation/

            rows[row].add(seat)

        # Every completely empty row can fit 2 groups
        ans = (n - len(rows)) * 2

        # Check rows that have reservations
        for seats in rows.values():

            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans
