class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        if len(nums) == 0: return res

        hashset = set()
        for n in nums:
            hashset.add(n)
        
        for n in hashset:
            if n-1 not in hashset:
                length = 1
                while n+length  in hashset:
                    length += 1
                
                res = max(res,length)
        
        return res