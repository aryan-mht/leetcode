from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = 0
        mapping = defaultdict(int)

        for num in nums: # O(n)
            mapping[num] += 1
        
        mapping = dict(sorted(mapping.items(), key=lambda x: x[1], reverse=True)) # mlogm (m unique items)
        for num in mapping: # O(m)
            if count < k:
                res.append(num)
                count += 1
            else:
                break
        
        return res # O(n + mlogm)
        
