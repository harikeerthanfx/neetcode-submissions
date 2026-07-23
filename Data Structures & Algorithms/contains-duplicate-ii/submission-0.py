class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {} #val:index
        
        for i,ch in enumerate(nums):
            if ch not in hash:
                hash[ch] = i
            else:
                if abs(hash[ch] - i) <= k:
                    return True
                else:
                    hash[ch] = i
        
        return False
            