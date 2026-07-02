class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Optimal Solutions with reverse loop
        # n = len(temperatures)
        # stack = []
        # res = [0]*n
        # for i in range(n-1,-1, -1):
        #     curr = temperatures[i]
        #     while stack and temperatures[stack[-1]] <= curr:
        #         stack.pop()
        #     if stack:
        #         res[i] = stack[-1] - i
        #     stack.append(i)

        # return res

        # 2 Optimal but with forward loop
        n = len(temperatures)
        res = [0]*n
        mono_stack = []
        for i in range(n):
            curr = temperatures[i]
            while mono_stack and temperatures[mono_stack[-1]] < curr:
                ind = mono_stack.pop()
                res[ind] = i-ind
            mono_stack.append(i)

        return res
