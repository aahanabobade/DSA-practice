# Implement Queue using Stacks
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.2 MB
# https://leetcode.com/problems/implement-queue-using-stacks/

        """
        return self.output_stack.pop()

        self.peek()
        
    def peek(self):
        """
        :rtype: int
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        :rtype: int
        """
    def pop(self):

        
        self.input_stack.append(x)
        """
        :rtype: None
        :type x: int
        """
