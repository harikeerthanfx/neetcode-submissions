class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for ch in s:
            if ch.isalnum():
                str += ch.lower()

        l, r = 0, len(str) - 1

        while l < r:
            if str[l] == str[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        return True
