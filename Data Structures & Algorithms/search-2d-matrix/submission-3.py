class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force with List comprehension Time Complexity: O(m*n) Space complexity: O(m*n)
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

        # Sub-Optimal Solution Time Complexity: O(m log n) Space Complexity: O(1)
        # for row in matrix:
        #     if row[-1] < target:
        #         continue
        #     else:
        #         lo, hi = 0, len(row) - 1
        #         while lo <= hi:
        #             mid = lo + (hi - lo)//2
        #             if row[mid] == target:
        #                 return True
        #             elif row[mid] > target:
        #                 hi = mid - 1
        #             else:
        #                 lo = mid + 1
            
        # return False

        # Optimal Solution Time Complexity: O(log m*n) Space Complexity: O(1)
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n - 1

        while lo <= hi:
            mid = lo + (hi - lo)//2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False