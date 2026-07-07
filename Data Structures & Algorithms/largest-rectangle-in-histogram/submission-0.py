class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            ptl, ptr = i-1, i+1
            curr = heights[i]
            while ptl > -1 and heights[ptl] >= heights[i]:
                curr += heights[i]
                ptl -= 1
            
            while ptr < len(heights) and heights[ptr] >= heights[i]:
                curr += heights[i]
                ptr += 1
            
            print(curr)
            
            res = max(res, curr)

        return res