class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if n < m or t == "":
            return ""

        countT = {}
        for i in range(m):
            if t[i] not in countT:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1

        window = {}
        for i in range(n):
            if s[i] not in window:
                window[s[i]] = 0

        have, need = 0, len(countT) 

        #----------------

        res, reslen = [-1,-1],float("infinity")
        l = 0

        for r in range(n):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update result
                if (r - l + 1) < reslen:
                    res = [l,r]
                    reslen = (r - l + 1)
                
                #pop from left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""

        
                    
            



                


            




        
    
        
        