class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        s = sorted(set(nums), reverse=True)
        
        if len(s) < 3:
            return s[0]
        
        return s[2]