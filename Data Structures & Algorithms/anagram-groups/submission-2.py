class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupStrs = {} # key - newStr(standardized string), value - [list of anagrams]

        for s in strs:
            newStr = ''.join(sorted(s))
            if newStr in groupStrs:
                groupStrs[newStr].append(s)
            else:
                groupStrs[newStr] = [s]
            
        final = []
        for key in groupStrs.keys():
            final.append(groupStrs[key])

        return final