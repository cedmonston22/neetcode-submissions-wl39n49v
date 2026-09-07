class Solution:
    def maxDifference(self, s: str) -> int:
        let_map = Counter(s)
        min_even = float("inf")
        max_odd = 0
        for value in let_map.values():
            if value % 2 == 0:
                if value < min_even:
                    min_even = value
            else:
                if value > max_odd:
                    max_odd = value
        return max_odd - min_even