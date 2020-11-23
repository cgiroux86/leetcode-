class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        flat = []
        result = 0
        for g in grid:
            flat+=g
        for f in flat:
            result+=1 if f < 0 else 0
        return result