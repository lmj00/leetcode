from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        pair = 0
        count = 0
        
        for i in Counter(nums).most_common():
            pair += i[1] // 2
            count += i[1] % 2
        
        
        return [pair, count]
                    