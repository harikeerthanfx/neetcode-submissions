class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        l = 0
        have = {}
        have[s[l]] = 1
        count = 1

        for r in range(1,len(s)):
            while s[r] in have:
                del have[s[l]]
                l += 1
            have[s[r]] = 1
            count = max(count, r-l+1)
        return count