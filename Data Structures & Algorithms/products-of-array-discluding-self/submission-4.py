class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count0 = 0
        for el in nums:
            if el == 0:
                if count0 == 1:
                    prod = 0
                    break
                count0 += 1
            else:
                prod *= el

        if prod == 0:
            return [0 for i in range(len(nums))]

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = prod
            else:
                if count0 == 1:
                    nums[i] = 0
                else:
                    nums[i] = prod//nums[i]
        return nums

