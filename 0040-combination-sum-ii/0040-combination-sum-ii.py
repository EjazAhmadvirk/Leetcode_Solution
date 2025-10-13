class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, s):
            if s > target:
                return
            if s == target:
                ans.append(t.copy())
                return
            for j in range(i, len(candidates)):
                # or: if i == j or candidates[j] != candidates[j - 1]
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                t.append(candidates[j])
                dfs(j + 1, s + candidates[j])
                t.pop()

        ans = []
        candidates.sort()
        t = []
        dfs(0, 0)
        return ans
