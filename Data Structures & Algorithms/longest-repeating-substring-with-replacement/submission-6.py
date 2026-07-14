class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        if len(s)==1:
            return 1

        l, r = 0, 1
        count[s[l]] = 1
        res, reslen = [-1,-1], 1

        for r in range(1,len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1

            largest = max(count, key = count.get)
            #largest is a character
            print(largest)

            while (r-l+1) - count[largest] > k:
                #while invalid
                if count[s[l]] == 1:
                    del count[s[l]]
                else:
                    count[s[l]] -= 1
                l += 1
                largest = max(count, key = count.get)
            
            #update ans 
            #valid condition -> if better,save -> expand
            temp = r - l + 1
            if reslen < temp:
                reslen = temp
                res = [l,r]
            r += 1
        
        return reslen





            