# Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Runtime: 197 ms
# Memory: 71.4 MB
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Step 3: Find maximum twin sum
        first = head
        second = prev
        ans = 0
        
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next
        
        return ans
