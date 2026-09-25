class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}

        for x in s:
            if x not in hashmap_s:
                hashmap_s[x] = 1
            else:
                hashmap_s[x] += 1
        for x in t:
            if x not in hashmap_t:
                hashmap_t[x] = 1
            else:
                hashmap_t[x] += 1

        if hashmap_s == hashmap_t:
            return True
        else:
            return False