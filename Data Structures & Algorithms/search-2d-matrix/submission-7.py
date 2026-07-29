class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m - 1
        row = -1
        while l <= r:
            mid = (l+r)//2

            if target >= matrix[mid][0]  and target <= matrix[mid][n-1] :
                row = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        
        if l > r:
            return False
        if row == -1:
            return False

        print(row)
        nl = 0
        nr = n - 1
        while nl <= nr:
            mid = (nl+nr)//2
            if matrix[row][mid] > target:
                nr = mid - 1
            elif matrix[row][mid] < target:
                nl = mid + 1
            else:
                return True
        
        return False

            
