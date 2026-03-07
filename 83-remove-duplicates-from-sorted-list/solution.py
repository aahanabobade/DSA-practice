# Remove Duplicates from Sorted List
# Difficulty: Easy
# Runtime: 5 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head
