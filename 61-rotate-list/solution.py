# Rotate List
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/rotate-list/

        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        #break
        
        return new_head
        
