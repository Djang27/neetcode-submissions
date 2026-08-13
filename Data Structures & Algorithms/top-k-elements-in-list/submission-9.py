class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #make hashmap to track freq
        count = {}
        #make list to group numbers under each cnt
        freq = [[] for i in range(len(nums) + 1)]

        #iterate through the list 
        for n in nums:
            #update hasmap with frequencies
            count[n] = 1 + count.get(n, 0)
        #then iterate through items of hashmap 
        for num, cnt in count.items():
            #update the groups of list
            freq[cnt].append(num)

        #make res list
        res = []

        #iterate through list from end to start, descending by 1
        for i in range(len(freq) - 1, 0, -1):
            #append most freq nums to res list
            for n in freq[i]:
                res.append(n)
                #if at any pt the res list is the same size as k
                if len(res) == k:
                    #return the res list
                    return res