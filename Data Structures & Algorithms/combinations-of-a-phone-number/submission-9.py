class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        numbers = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }

        res = []
        # "",0,0
        def dfs(dial,idx): #l is the index of which character from the number 2abc we are curr on
            if idx == len(digits):
                res.append(dial)
                return
            
            n = int(digits[idx])
            for ch in numbers[n]:
                dfs(dial+ch,idx+1)
        
        dfs("",0)
        return res
            