class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(par, op, cl):
            if op == cl and op == n:
                res.append("".join(par))
                return

            if op < n and op > cl:
                # two choices
                par.append("(")
                dfs(par, op + 1, cl)
                par.pop()

                par.append(")")
                dfs(par, op, cl + 1)
                par.pop()

            elif op == cl:
                # only "(" choice
                par.append("(")
                dfs(par, op + 1, cl)
                par.pop()

            elif op == n:
                # only ")" choice
                par.append(")")
                dfs(par, op, cl + 1)
                par.pop()

        dfs([], 0, 0)
        return res