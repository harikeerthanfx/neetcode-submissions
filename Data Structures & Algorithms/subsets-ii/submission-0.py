class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        completed = set()

        def dfs(i,subset):
            if tuple(subset) in completed:
                return
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1,subset)

            subset.pop()
            dfs(i+1,subset)

            completed.add(tuple(subset))

        dfs(0,[])
        return res