class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupStr = {}

        for s in strs:
            newStr = ''.join(sorted(s))
            if newStr in groupStr:
                groupStr[newStr].append(s)
            else:
                groupStr[newStr] = [s]
        
        final = []
        for key in groupStr.keys():
            final.append(groupStr[key])
        
        return final