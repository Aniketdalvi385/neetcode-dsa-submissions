class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for car in cars:
            time = (target - car[0])/car[1]
            print(time)
            if not stack or stack[-1] < time:
                stack.append(time)

        print(stack)
        return len(stack)