class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = [i for i in s]
        t = [i for i in t]

        s.sort()
        t.sort()

        for i in range(len(s)):        
            if s[i] != t[i]:
                return t[i]
        
        return t[-1]