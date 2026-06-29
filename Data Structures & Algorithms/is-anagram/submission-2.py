class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_t="".join(sorted(t))
        sorted_s="".join(sorted(s))

        if sorted_t == sorted_s: 
            return True
        else:
            return False