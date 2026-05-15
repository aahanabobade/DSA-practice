# Min Stack
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 15.7 MB
# https://leetcode.com/problems/min-stack/

    def pop(self):

        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)


    def push(self, val):

        self.minStack = []
        self.stack = []
    def __init__(self):

class MinStack(object):

