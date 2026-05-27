class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {} #initialze a hashtable(dict) for both

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #.get() -> returns value of key
            countT[t[i]] = 1 + countT.get(t[i], 0) # must use .get() since value isn't already initalized
        return countS == countT