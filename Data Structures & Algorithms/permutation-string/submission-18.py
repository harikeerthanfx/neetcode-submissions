class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2 : return False

        hash1 = {}

        for i,ch in enumerate(s1):
            hash1[ch] = 1 + hash1.get(ch,0)
        
        l = 0
        hash2 = {}
        hash2[s2[l]] = 1
        if hash2 == hash1: return True

        for r in range(l+1,n2,1):
            if r - l + 1 > n1:
                if hash2[s2[l]] == 1:
                    del hash2[s2[l]]
                else:
                    hash2[s2[l]] -= 1
                l += 1
            
            hash2[s2[r]] = 1 + hash2.get(s2[r],0)

            if hash2 == hash1:
                return True
        
        return hash2 == hash1
                

