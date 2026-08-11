class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        freq = {} # value : frequency

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        return sorted(freq, key = freq.get, reverse = True)[:k]