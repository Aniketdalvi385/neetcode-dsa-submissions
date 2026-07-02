class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0]*n
        for i in range(n-1,-1, -1):
            curr = temperatures[i]
            while stack and temperatures[stack[-1]] <= curr:
                stack.pop()
            if stack and temperatures[stack[-1]] > curr:
                res[i] = stack[-1] - i
            stack.append(i)

        return res
