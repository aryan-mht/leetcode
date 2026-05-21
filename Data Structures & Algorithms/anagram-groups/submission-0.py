class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for x in strs:
            sorted_str = sorted(x)
            sorted_str = "".join(sorted_str)
            if sorted_str in anagramMap:
                anagramMap[sorted_str].append(x)
            else:
                anagramMap[sorted_str] = [x]
        
        return list(anagramMap.values())
    