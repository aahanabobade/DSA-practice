# Implement Stack using Queues
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/implement-stack-using-queues/

        :rtype: int
        """
        
        return self.input_queue[0]

    def empty(self):
        """
        :rtype: bool
        """


        return len(self.input_queue)==0
        
        """
    def top(self):
        

        return self.input_queue.pop(0)
        :rtype: int
        """
        """
    def pop(self):

