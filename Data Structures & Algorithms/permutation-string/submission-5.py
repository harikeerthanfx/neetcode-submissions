class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        need = {}
        for ch in s1:
            need[ch] = 1 + need.get(ch, 0)

        have = {}
        l = 0

        for r in range(n2):
            # ADD
            have[s2[r]] = 1 + have.get(s2[r], 0)

            # SHRINK IF WINDOW > K
            if (r - l + 1) > n1:
                have[s2[l]] -= 1

                if have[s2[l]] == 0:
                    del have[s2[l]]

                l += 1

            # CHECK FIXED WINDOW
            if (r - l + 1) == n1:
                if have == need:
                    return True

        return False