class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 : return 0
        
        l = 0
        count = {}

        count[s[l]] = 1
        maxlen = 1

        for r in range(l+1,len(s),1):
            while s[r] in count:
                del count[s[l]]
                l += 1
            
            if s[r] not in count:
                count[s[r]] = 1
            
            maxlen = max(maxlen,r-l+1)
            

        return maxlen


