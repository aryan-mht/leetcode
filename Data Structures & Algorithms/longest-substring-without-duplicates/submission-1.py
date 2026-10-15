class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_length = 0
        window = set()
        while r < len(s):
            if s[r] in window:
                while l <= r and s[r] in window:
                    window.remove(s[l])
                    l+=1
            else:
                window.add(s[r])
                r+=1
                max_length = max(max_length, len(window))
        return max_length
            
# LC 3: Make a window with l and r. Grow it from the right. If a letter repeats, shrink from the left until it's gone. Keep track of the biggest it ever got.

            
        