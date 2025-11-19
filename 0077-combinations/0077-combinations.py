class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, t):
            # no need to check len(t)>k, when '==k' returned already
            if len(t) == k:
                res.append(t.copy())
                return
            for j in range(i, n + 1):
                t.append(j)
                dfs(j + 1, t)
                t.pop()

        dfs(1, []) # 1 to n
        return res

class Solution_iteration:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        out = [0] * k
        i = 0
        
        while i >= 0:
            out[i] += 1
            if out[i] > n:
                i -= 1
            elif i == k - 1:
                res.append(list(out))
            else:
                i += 1
                out[i] = out[i - 1]
                
        return res

