# Merge k Sorted Lists
# Difficulty: Hard
# Runtime: 12 ms
# Memory: 18.2 MB
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        heap = []

        for i ,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i, node)) 
        
        D =ListNode()
        cur = D

        while heap :
            val, i ,node =heapq.heappop(heap)
            cur.next =node
            cur = node
            node =node.next
            if node:
                heapq.heappush(heap,(node.val,i, node)) 
        
        return D.next
