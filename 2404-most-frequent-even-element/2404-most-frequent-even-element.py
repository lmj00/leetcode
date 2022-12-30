from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        v = list(filter(lambda x: x[0] % 2 == 0, Counter(sorted(nums)).most_common()))

        return -1 if len(v) == 0 else v[0][0]