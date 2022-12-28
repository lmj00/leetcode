from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        for i in Counter(nums).most_common():
            if i[1] % 2 != 0:
                return False
        
        return True