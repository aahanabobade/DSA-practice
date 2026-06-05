# Remove Nth Node From End of List
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        #make dummy node which points to next
        #two pointer : at dummy node(ahead and behind)
        #d->n1->n2...
        #ahead = n+1
        #behind : dummy
        dummy = ListNode()
        dummy.next =head
        behind = ahead = dummy

        for _ in range(n+1): #n inclusive
            ahead = ahead.next
        
        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next #will be always valid bcz 1 <= sz <= 30
        return dummy.next

        