class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for string in strs:
            enc += str(len(string)) + "#" + string
        return enc

    def decode(self, s: str) -> List[str]:
        res = []
        count = len(s)
        i = 0
        while i < count:
            length = ""
            digits = 0
            while not s[i] == "#":
                length += s[i]
                digits += 1
                i+=1
            intlength = int(length)
            string = s[i+1:i+intlength+1]
            res.append(string)
            i += intlength + 1
        return res




                
