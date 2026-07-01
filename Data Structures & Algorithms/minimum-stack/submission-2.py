class MinStack:

    def __init__(self):
        self.og = []
        self.low = []

    def push(self, val: int) -> None:
        self.og.append(val)
        if not self.low or val <= self.low[-1]:
            self.low.append(val)
        return None

    def pop(self) -> None:
        if self.low and (self.og[-1] == self.low[-1]):
            self.low.pop()
        self.og.pop()
        return None

    def top(self) -> int:
        return self.og[-1]

    def getMin(self) -> int:
        return self.low[-1]
