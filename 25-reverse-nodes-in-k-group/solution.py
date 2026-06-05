# Reverse Nodes in k-Group
# Difficulty: Hard
# Runtime: 3 ms
# Memory: 14.3 MB
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        d = ListNode(0,head)
        groupprev = d

        while True:
            kth = self.getk(groupprev,k)
            if not kth:
                break
            groupnext = kth.next

            prev ,curr =kth.next, groupprev.next

            while curr!=groupnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp

        return d.next


    
    def getk(self,curr,k):
        while curr and k >0:
            curr = curr.next
            k -= 1
        return curr



