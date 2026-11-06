class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []

        for i in range(len(speed)):
            cars.append((position[i],speed[i]))
        
        for c in sorted(cars, reverse=True):
            pos, spd = c
            stack.append((target-pos)/spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)