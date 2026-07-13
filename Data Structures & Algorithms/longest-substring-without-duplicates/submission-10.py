class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        once = {}

        l,r = 0, 1
        once[s[l]] = 1
        res, reslen = [-1,-1], 0

        while r < len(s):
            if s[r] not in once:
                #valid window -> expand
                once[s[r]] = 1
                length = r - l + 1
                if length > reslen:
                    res = [l,r]
                    reslen = length
                r += 1
            else : 
                #invaid window -> shrink 
                if once[s[l]] == 1:
                    del once[s[l]]
                else:
                    once[s[l]] -= 1
                l += 1
        return reslen

