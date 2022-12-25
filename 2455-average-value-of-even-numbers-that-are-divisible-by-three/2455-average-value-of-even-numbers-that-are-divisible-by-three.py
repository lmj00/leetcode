class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        v = 0
        count = 0
        
        for i in nums:
            if i % 6 == 0:
                v += i
                count += 1
                
        return 0 if v == 0 else v // count 