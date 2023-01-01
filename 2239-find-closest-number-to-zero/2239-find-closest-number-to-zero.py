class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        nums2 = nums
        nums = sorted(list(map(abs, nums)))
        
        if nums[0] in nums2:
            return nums[0]

        return -nums[0]