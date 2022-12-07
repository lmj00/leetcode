class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        odd_ls = []
        even_ls = []
        
        for i in nums:
            if i % 2 == 1:
                odd_ls.append(i)
            else:
                even_ls.append(i)
        
        even_ls += odd_ls
        
        return even_ls