class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        for car in sorted(cars,reverse=True):
            pos, spd = car
            stack.append((target-pos)/spd)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)