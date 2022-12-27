class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        val = -1
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    val = max(val, nums[i] - nums[j])                       
                    
        return val
