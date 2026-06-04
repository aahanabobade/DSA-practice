# Insert Delete GetRandom O(1)
# Difficulty: Medium
# Runtime: 163 ms
# Memory: 56.6 MB
# https://leetcode.com/problems/insert-delete-getrandom-o1/


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)
        return True
        self.map[last]=idx
        self.list[idx] =last

        last= self.list[-1]
        idx = self.map[val]


        self.list.pop() 
        del self.map[val]

