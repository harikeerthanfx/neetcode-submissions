class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for word in strs:
            string = string + str(len(word)) + '#' + word
        return string


    def decode(self, s: str) -> List[str]:
        list_return =[]
        i = 0

        while i<len(s) :
            j = i
            while s[j]!='#':
                j+=1
            length_of_word=int(s[i:j])
        
            i=j+1

            word=s[i:i+length_of_word]
            list_return.append(word)

            i=i+length_of_word
        
        return list_return


