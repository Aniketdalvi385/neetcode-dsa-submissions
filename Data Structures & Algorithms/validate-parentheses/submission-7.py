class Solution:
    def isValid(self, s: str) -> bool:
        # Brute force
        # if len(s)%2 != 0:
        #     return False
        # curr = deque()
        # for i in s:
        #     print(curr)
        #     if i == '[' or i == '(' or i == '{':
        #         curr.append(i)
        #     else:
        #         if i == ']' and curr:
        #             if curr[-1] != '[':
        #                 return False
        #             else:
        #                 curr.pop()
        #         elif i == ')' and curr:
        #             if curr[-1] != '(':
        #                 return False
        #             else:
        #                 curr.pop()
        #         elif i == '}' and curr:
        #             if curr[-1] != '{':
        #                 return False
        #             else:
        #                 curr.pop()
        #         else:
        #             return False
        # if curr:
        #     return False
        
        # return True

        hashmap = {')': '(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if ch in hashmap:
                if not stack or stack[-1] != hashmap[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        if stack:
            return False

        return True


