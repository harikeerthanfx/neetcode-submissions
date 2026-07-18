class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 == 0:
            return True

        count1 = {}
        for ch in s1:
            count1[ch] = 1 + count1.get(ch,0)

        count2 = {}

        l = 0
        for r in range(n2):
            count2[s2[r]] = 1 + count2.get(s2[r],0)
            if (r-l+1) > n1:
                print(l,r,n1)
                if count2[s2[l]] == 1:
                    del count2[s2[l]]
                else:
                    count2[s2[l]] -= 1
                l += 1
            if (r-l+1) == n1:
                if count2 == count1:
                    return True
        return False


