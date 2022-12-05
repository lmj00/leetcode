class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        ls = []
        i = 0
        
        while i < len(nums):
            if nums[i] == 0:
                ls.append(0)
                del nums[i]
                i -= 1
            i += 1
            
        nums += ls