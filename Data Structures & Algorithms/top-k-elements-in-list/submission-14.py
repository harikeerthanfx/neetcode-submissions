class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        arr = [[] for i in range(n+1)]
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num,0)

        for n, c in count.items():
            arr[c].append(n)



        for el in reversed(arr):
            for n in el:
                res.append(n)
                if len(res) == k:
                    return res