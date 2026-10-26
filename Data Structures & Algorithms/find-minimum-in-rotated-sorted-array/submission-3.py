class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = -1

        l, r = 0, len(nums)-1

        while(l<=r):
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                res = nums[mid]
                if nums[mid-1] < nums[mid]:
                    r = mid - 1
                else:
                    return res
            elif l==r:
                return nums[l]
        return res