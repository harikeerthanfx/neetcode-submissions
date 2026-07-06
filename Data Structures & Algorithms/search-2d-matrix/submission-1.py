class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows-1
        while(l<=r):
            mid = (l+r)//2
            if matrix[mid][0] > target:
                r = mid-1
            elif matrix[mid][cols-1] < target:
                l = mid+1
            else:
                break
        
        if l>r:
            return False

        row = (l+r)//2
        print(row)

        nl, nr = 0, cols-1
        while(nl<=nr):
            mid = (nl+nr)//2

            if matrix[row][mid] > target:
                nr = mid - 1
            elif matrix[row][mid] < target:
                nl = mid + 1
            elif matrix[row][mid] == target:
                print(mid)
                return True
        return False
        
            


