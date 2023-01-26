class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        m = 0
        p = 0
        
        for i in nums:
            if i < 0:
                m += 1
            elif i > 0:
                p += 1
        
        return max(m, p)