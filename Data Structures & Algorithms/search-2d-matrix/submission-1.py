class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [num for row in matrix for num in row]
        lo, hi = 0, len(arr)-1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
            
        return False