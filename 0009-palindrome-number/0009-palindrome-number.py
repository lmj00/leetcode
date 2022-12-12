class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        j = 0
                
        for i in range(len(x) - 1, -1, -1):
            if x[j] != x[i]:
                return False
            j += 1
            
        return True