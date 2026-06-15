# Delete the Middle Node of a Linked List
# Difficulty: Medium
# Runtime: 72 ms
# Memory: 91.5 MB
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
