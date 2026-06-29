class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string = string + str(len(word)) + "#" + word
        print(string)
        return string
        
    def decode(self, s: str) -> List[str]:
        list_return = []

        i=0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            word_len = int(s[i:j])

            word = s[j+1:j+1+word_len]
            list_return.append(word)
            i = j + 1 + word_len 

        print(s)
        return list_return
