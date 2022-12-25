class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        nums.sort()
        i = len(nums) - 1
        
        while True:
            if i < 0:
                return -1
            
            if -nums[i] in nums:
                return nums[i]
            
            i -= 1
    