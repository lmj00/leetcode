from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
         
        v = list(filter(lambda x: x[1] == 1, Counter(nums).most_common()))
        result = 0
        
        for i in v:
            result += i[0]
        
        return result