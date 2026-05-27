class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:

            stn = ''.join(sorted(s))

            if stn not in groups:
                
                groups[stn] = [s]
            
            else:
                
                curr = groups[stn]
                curr.append(s)
                groups[stn] = curr

        final = []
        for key in groups.keys():
            final.append(groups[key])

        return final
