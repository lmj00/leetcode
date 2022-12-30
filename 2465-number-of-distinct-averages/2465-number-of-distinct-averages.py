class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        result = []
        nums.sort()
        
        for i in range(len(nums) // 2):
            result.append((nums[i] + nums[len(nums) - i - 1]) / 2)

        return 1 if len(nums) == 2 else len(set(result))
