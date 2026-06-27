class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m*n-1

        while lo<=hi:
            mid = (lo+hi)//2

            row,col = mid//n,mid%n

            mid_num = matrix[row][col]
            if mid_num==target:
                return True
            elif mid_num<target:
                lo=mid+1
            else:
                hi = mid-1
        
        return False
        