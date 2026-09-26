class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            res = res + str(n) + "*"  + s

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            n = ""
            while not s[i] == "*":
                n = n + s[i]
                i += 1
            
            num = int(n)
            res.append(s[i+1:i+1+num])
            i = i + 1 + num
        
        return res
