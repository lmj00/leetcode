class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        
        v = list(filter(lambda x: nums[x] == 1, range(len(nums))))
        
        for i in range(1, len(v)):
            if v[i] - v[i - 1] - 1 < k:
                return False
        
        return True
            
