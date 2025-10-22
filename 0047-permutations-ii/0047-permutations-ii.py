class Solution: # iterative
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the input to handle duplicates
        res = [[]]
        for num in nums:
            new_res = []
            for perm in res:
                for i in range(len(perm) + 1):
                    if i > 0 and perm[i - 1] == num:
                    # added for lc-47, as explained above "Why the Condition Works"
                        break # skip duplicate
                    new_perm = perm[:i] + [num] + perm[i:]
                    # or perm.insert(index, num), like in lc-46
                    new_res.append(new_perm)
            res = new_res
        return res
