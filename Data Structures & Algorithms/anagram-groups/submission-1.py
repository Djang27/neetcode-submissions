class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupStrs = {}
        # key - standardized str, value - [anagrams]
        for s in strs:
            # sort each string 
            newStr = ''.join(sorted(s))
            # check if standard string is groupStrs
            if newStr not in groupStrs:
                # if not 
                groupStrs[newStr] = [s]
                # update groupStrs
            else:
                groupStrs[newStr].append(s)
            # if already in groupsStrs
                # update groupStrs[s]
        
        final = [] 
        for key in groupStrs.keys():
            final.append(groupStrs[key])

        return final
