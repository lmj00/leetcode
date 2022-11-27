class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        nums = ''.join(str(s) for s in nums)

        return len(max(nums.split("0")))