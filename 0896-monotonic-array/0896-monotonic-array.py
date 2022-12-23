class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        asc = nums.copy()
        desc = nums.copy()
        
        asc.sort()
        desc.sort(reverse=True)
        
        
        return nums == asc or nums == desc