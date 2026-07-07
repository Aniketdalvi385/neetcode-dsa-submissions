class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute Force approach with O(n^2) Complexity
        # res = 0
        # for i in range(len(heights)):
        #     ptl, ptr = i-1, i+1
        #     width = 1
        #     while ptl > -1 and heights[ptl] >= heights[i]:
        #         width += 1
        #         ptl -= 1
            
        #     while ptr < len(heights) and heights[ptr] >= heights[i]:
        #         width += 1
        #         ptr += 1
            
        #     res = max(res, heights[i]*width)

        # return res

        maxArea = 0
        mono_stack = []

        for i, h in enumerate(heights):
            start = i
            while mono_stack and mono_stack[-1][1] > h:
                ind, ht = mono_stack.pop()
                width = i - ind
                area = width * ht
                maxArea = max(area, maxArea)
                start = ind
            mono_stack.append((start, h))

        while mono_stack:
            ind, ht = mono_stack.pop()
            width = len(heights) - ind
            area = width * ht
            maxArea = max(area, maxArea)

        return maxArea