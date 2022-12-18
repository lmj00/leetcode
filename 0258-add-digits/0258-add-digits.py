class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while len(str(num)) > 1:

            num = [int(i) for i in str(num)]
            num = sum(num)
        
            
            
        return num