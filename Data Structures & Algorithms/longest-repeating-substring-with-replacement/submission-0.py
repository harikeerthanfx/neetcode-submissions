class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)

        hashMap = {}
        for ch in s:
            hashMap[ch] = 0
        
        l , r = 0 , 0
        max_len = 0
        hashMap[s[l]] = 1

        while r < len(s) - 1:
            r += 1
            hashMap[s[r]] += 1

            max_char_count= 0
            max_char = "z"
            for ch in hashMap:
                if hashMap[ch] > max_char_count:
                    max_char_count = hashMap[ch]
                    max_char = ch
            
            if r-l+1 - max_char_count <= k:
                if max_len < r-l+1:
                    max_len = r-l+1
            else:
                l += 1
                hashMap[s[l-1]] -= 1
        return max_len