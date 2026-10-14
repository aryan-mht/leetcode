from typing import List
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] += 1
        
        for num, f in count.items():
            freq[f].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for s in freq[i]:
                res.append(s)
                if len(res) == k:
                    return res
        return res
        
        
    
        
