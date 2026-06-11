class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["act","pots","tops","cat","stop","hat"]
        '''
        act: [act, cat]
        opts: [pots, tops, stop]
        aht: [hat]
        '''
        res = {}
        for word in strs: # O(m)
            key = ''.join(sorted(word)) # O(nlogn) where n is the size of word
            if key not in res:
                res[key] = []
            res[key].append(word)
        
        return list(res.values())
        
        # total time: O(m * nlogn)
    