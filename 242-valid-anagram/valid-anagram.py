class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = len(s)
        t1= len(t)
        freq = {}

        if s1 != t1:
            return False

        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1

        for char in t:
            if char not in freq:
                return False
            freq[char]-=1
            if freq[char]<0:
                return False

        
        
        
        return True
        


        