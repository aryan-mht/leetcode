class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmapS = {}
        hashmapT = {}
        for char in s: 
            hashmapS[char] = hashmapS.get(char, 0) + 1
        
        for char in t: 
            hashmapT[char] = hashmapT.get(char, 0) + 1
        
        # s = cat
        # 0 1 2
        return hashmapS == hashmapT
        
        