class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        val = -1
        max_v = nums[-1]
        
        for i in range(len(nums) -2, -1, -1):
            if nums[i] >= max_v:
                max_v = nums[i]
            else:
                val = max(val, max_v - nums[i])                       
            
        return val
    