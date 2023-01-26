class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        a = sum(nums)
        b = ''
        
        for i in nums:
            b += str(i)

        b = sum(list(map(int, b)))
        
        return a - b
        
        