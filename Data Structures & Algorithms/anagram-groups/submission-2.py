class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs: # O(n)
            count = [0] * 26 # each word will have a unique count signature [1, 0, .., 1, 0]
            # use that sig as key
            for char in word: # O(k)
                index = ord(char) - ord('a') # index 0 = a, 1 = b....
                count[index] += 1
            res[tuple(count)].append(word)
        
        return list(res.values()) # O(k*n)