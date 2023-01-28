class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ls = []
        
        for idx, v in enumerate(nums):
            ls.append(sum(nums[:idx + 1]))
        
        return ls