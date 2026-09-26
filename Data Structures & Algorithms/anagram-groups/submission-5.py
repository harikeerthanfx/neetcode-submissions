class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anag = {}
        res = []

        for word in strs:
            if "".join(sorted(word)) in anag:
                anag["".join(sorted(word))].append(word)
            else:
                anag["".join(sorted(word))] = [word]
        
        for anagrams in anag:
            res.append(anag[anagrams])

        return res
