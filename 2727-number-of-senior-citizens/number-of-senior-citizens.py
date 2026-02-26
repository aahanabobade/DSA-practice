class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        n = len(details)
        count = 0

        for i in range(n):
            age = int(details[i][11:13])
            if age > 60:
                count +=1
        
        return count
        