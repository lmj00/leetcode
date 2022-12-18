class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while len(str(num)) > 1:
            
            num = [i for i in str(num)]
            num = '+'.join(num)
            num = eval(num)
                
        return num