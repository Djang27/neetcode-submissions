class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numHistory = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numHistory:
                return[numHistory[diff], i]
            numHistory[n] = i