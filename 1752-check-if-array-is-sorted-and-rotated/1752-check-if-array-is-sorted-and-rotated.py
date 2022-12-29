from collections import deque

class Solution:
    def check(self, nums: List[int]) -> bool:
        
        dq = deque(nums)
        count = 0
        
        while count < len(dq):
            dq.rotate(-1)
            count += 1
            
            if list(dq) == sorted(nums):
                return True
            
        return False