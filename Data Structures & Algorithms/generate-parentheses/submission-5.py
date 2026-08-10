class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(par, op, cl):
            if op == cl == n:
                res.append("".join(par))
                return

            if op < n :
                par.append("(")
                dfs(par, op + 1, cl)
                par.pop()

            if cl < op:
                # only ")" choice
                par.append(")")
                dfs(par, op, cl + 1)
                par.pop()

        dfs([], 0, 0)
        return res