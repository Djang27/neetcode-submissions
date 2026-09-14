class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hist = {} # values: index 

        for i, n in enumerate(nums): # i - index, n - value
            diff = target - n
            if diff in hist:
                return [hist[diff], i]
            else:
                hist[n] = i
        return []