from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        
        nums1 += nums2 + nums3
        
        ls = list(filter(lambda x: x[1] > 1, Counter(nums1).most_common()))
        
        return [i[0] for i in ls]