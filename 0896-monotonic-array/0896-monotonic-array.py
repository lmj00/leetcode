class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        nums2 = nums.copy()
        nums2.sort()
        
        return nums == nums2 or nums == list(reversed(nums2))