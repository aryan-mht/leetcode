class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_found = 0
        while i < j:
            width = j - i
            area = width * min(heights[i], heights[j])
            if area > max_found:
                max_found = area
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return max_found
            