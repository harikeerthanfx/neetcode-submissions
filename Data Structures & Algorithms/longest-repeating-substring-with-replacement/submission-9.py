class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        if len(s)==1:
            return 1

        l, r = 0, 1
        count[s[l]] = 1
        res, reslen = [-1,-1], 1

        for r in range(1,len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                largest = max(count.values())
            
            reslen = max(reslen, r-l+1)
            r += 1
        
        return reslen





            