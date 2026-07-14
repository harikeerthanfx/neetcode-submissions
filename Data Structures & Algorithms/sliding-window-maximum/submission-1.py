class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        for r in range(len(nums)):
            if (r-l+1) > k:
                l += 1
            if (r-l+1) == k:
                largest = max(nums[l:r+1])
                res.append(largest)
        
        return res