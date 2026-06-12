import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HEAP SOLUTION
        # ═══════════════════════════════════════════════
        # STEP 1: Count frequencies
        # Data Structure: Dictionary (Hash Map)
        # Time Complexity: O(n) — visit every element once
        # ═══════════════════════════════════════════════
        count = defaultdict(int)
        for num in nums: 
            count[num] += 1
        # after this step, count looks like:
        # nums = [1,1,1,2,2,3] → count = {1:3, 2:2, 3:1}

        # ═══════════════════════════════════════════════
        # STEP 2: Maintain a min-heap of size k
        # Data Structure: Min-Heap (heapq in Python)
        # Time Complexity: O(n log k)
        #   — n elements to process
        #   — each push/pop costs log k (heap size never exceeds k)
        # 
        # WHY MIN-HEAP?
        #   root is always the LOWEST frequency
        #   so when heap is too big, we kick out the least frequent
        #   this keeps only the TOP k frequent elements
        #
        # WHY TUPLE (freq, num)?
        #   heapq sorts by first element → sorts by frequency
        #   num is carried along as passenger
        # ═══════════════════════════════════════════════

        heap = []                               # our heap, starts empty
        for num, freq in count.items():         # loop through every (number, frequency) pair
            heapq.heappush(heap, (freq, num))   # push (freq, num) — heap orders by freq
            
            if len(heap) > k:                   # heap too big?
                heapq.heappop(heap)             # remove the MINIMUM freq (root)
                                                # this evicts the least frequent element
        # after this step, heap contains exactly k most frequent elements
        # e.g. k=2 → heap = [(2,2), (3,1)]

        # ═══════════════════════════════════════════════
        # STEP 3: Extract just the numbers from the heap
        # Time Complexity: O(k) — loop through k elements
        # ═══════════════════════════════════════════════    
        return [num for freq,num in heap]


    # ═══════════════════════════════════════════════
    # OVERALL COMPLEXITY
    # Time:  O(n log k)
    #   Step 1: O(n)
    #   Step 2: O(n log k)   ← dominates
    #   Step 3: O(k)
    #
    # Space: O(n + k)
    #   O(n) for the count dictionary
    #   O(k) for the heap
    # ═══════════════════════════════════════════════
