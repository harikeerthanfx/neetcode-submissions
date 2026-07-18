class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)

        if n == 1:
            return 1

        l, r = 0 ,1
        count = {}
        count[s[l]] = 1
        res = 0
        for r in range(1,n):
            while s[r] in count:
                del count[s[l]]
                l += 1
            count[s[r]] = 1
            if r-l+1 > res:
                res = r - l + 1
        return res