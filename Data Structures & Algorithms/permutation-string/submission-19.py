class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}

        for ch in s1:
            need[ch] = 1 + need.get(ch,0)

        l = 0

        for r in range(len(s2)):
            #add to window
            window[s2[r]] = 1 + window.get(s2[r],0)

            #check window size
            if r-l+1 < len(s1):
                continue
            elif r-l+1 == len(s1):
                if window == need:
                    return True
                else:
                    if window[s2[l]] == 1:
                        del window[s2[l]]
                    else:
                        window[s2[l]] -= 1
                    l += 1
        return False