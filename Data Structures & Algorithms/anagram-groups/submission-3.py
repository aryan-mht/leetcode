class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            char_code = [0]*26
            for ch in s:
                idx = ord(ch) - ord('a')
                char_code[idx] += 1
            mapping[tuple(char_code)].append(s)
        
        return list(mapping.values())
            
