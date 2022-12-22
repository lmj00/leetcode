class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        ls = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                ls.append(abs(i - start))
                
        ls.sort()
                
        return ls[0]