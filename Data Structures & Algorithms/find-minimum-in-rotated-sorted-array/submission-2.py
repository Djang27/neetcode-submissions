class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        small = nums[0]

        for num in nums:
            small = min(small, num)
        return small