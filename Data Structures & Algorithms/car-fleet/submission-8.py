class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Optimal Solution Time complexity: O(n log n) Space Complexity: O(n)
        # cars = sorted(zip(position, speed), reverse=True)
        # stack = []
        # for car in cars:
        #     time = (target - car[0])/car[1]
        #     if not stack or stack[-1] < time:
        #         stack.append(time)

        # return len(stack)

        # Second Approach with simple hashmap to sorted. The complexities remain same we just change the logic to be more intuitive.
        hashmap = {}
        for i in range(len(position)):
            hashmap[position[i]] = speed[i]

        position.sort(reverse=True)
        prev = 0
        count = 0
        for car in position:
            time = (target - car)/hashmap[car]
            if prev < time:
                count += 1
                prev = time
        
        return count