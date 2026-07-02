class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip('+-').isnumeric():
                stack.append(int(t))
            else:
                if t == '+':
                    stack.append(int(stack.pop()+stack.pop()))
                elif t == '-':
                    curr = stack.pop()
                    stack.append(int(stack.pop()-curr))
                elif t == '*':
                    stack.append(int(stack.pop()*stack.pop()))
                elif t == '/':
                    curr = stack.pop()
                    stack.append(int(stack.pop()/curr))
        
        return stack.pop()