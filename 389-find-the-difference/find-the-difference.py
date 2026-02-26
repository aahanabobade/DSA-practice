class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        m = len(t)
        count = {}

        for i in range (n):
            if s[i] in count:
                count[s[i]] +=1
            else:
                count[s[i]] =1
            
        for j in range(m):
            if t[j] not in count:
                return t[j]
            
            count [t[j]]-=1

            if count[t[j]]<0:
                return t[j]
            
        


            