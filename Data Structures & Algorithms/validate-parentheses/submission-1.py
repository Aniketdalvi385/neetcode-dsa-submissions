class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        curr = deque()
        for i in s:
            print(curr)
            if i == '[' or i == '(' or i == '{':
                curr.append(i)
            else:
                if i == ']' and curr:
                    if curr[-1] != '[':
                        return False
                    else:
                        curr.pop()
                elif i == ')' and curr:
                    if curr[-1] != '(':
                        return False
                    else:
                        curr.pop()
                elif i == '}' and curr:
                    if curr[-1] != '{':
                        return False
                    else:
                        curr.pop()
                else:
                    return False
        if curr:
            return False
        
        return True