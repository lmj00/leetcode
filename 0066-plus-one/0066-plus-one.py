class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        ls = []
        num = ""
        
        for i in digits:
            num += str(i)
            
        num = str(int(num) + 1)

        ls += [int(i) for i in num]
        
        return ls