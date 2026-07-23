class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        have = set()

        for n in nums:
            if n in have:
                return True
            have.add(n)
        
        return False
