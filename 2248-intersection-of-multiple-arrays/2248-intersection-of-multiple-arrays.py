class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
                
        v = set(nums[0])
        
        for i in range(1, len(nums)):
            v = v & set(nums[i])
        
        return sorted(v)