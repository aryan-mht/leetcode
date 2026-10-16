class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= merged[-1][1]: 
                merged_start = min(start, merged[-1][0])
                merged_end = max(end, merged[-1][1])
                merged[-1] = [merged_start, merged_end]
            else:
                merged.append([start, end])
        
        return merged
        