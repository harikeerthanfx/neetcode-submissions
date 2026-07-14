class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        need = {}
        for ch in s1:
            need[ch] = 1 + need.get(ch,0)

        have = {}
        countneed = len(need)
        counthave = 0

        l = 0
        for r in range(n2):
            #ADD
            have[s2[r]] = 1 + have.get(s2[r],0)
            
            if (r-l+1) > n1:
                #remove left
                if have[s2[l]] == 1:
                    del have[s2[l]]
                else:
                    have[s2[l]] -= 1
                #inc l
                l += 1
                
            if (r-l+1) == n1:
                if have == need:
                    return True
        return False
                

            
                
            


            




