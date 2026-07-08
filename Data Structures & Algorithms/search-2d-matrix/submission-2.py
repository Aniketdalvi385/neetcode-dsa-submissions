class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force with List comprehension Time Complexity: O(log m*n) Space complexity: O(m*n)
        # arr = [num for row in matrix for num in row]
        # lo, hi = 0, len(arr)-1
        # while lo <= hi:
        #     mid = lo + (hi - lo)//2
        #     if arr[mid] == target:
        #         return True
        #     elif arr[mid] > target:
        #         hi = mid - 1
        #     else:
        #         lo = mid + 1
            
        # return False

        for row in matrix:
            if row[-1] < target:
                continue
            else:
                lo, hi = 0, len(row) - 1
                while lo <= hi:
                    mid = lo + (hi - lo)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            
        return False