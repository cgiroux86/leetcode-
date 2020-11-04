from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        def dft(heights, bricks, ladders, index, cache):

            usingBricks = 0
            usingLadders = 0
            if index == len(heights) - 1:
                return 0
            if bricks < 0 or ladders < 0:
                return 0
            if index not in cache:
                if heights[index] >= heights[index + 1]:
                    cache[index] = 1 + \
                        dft(heights, bricks, ladders, index + 1, cache)
                else:
                    if bricks - (heights[index + 1] - heights[index]) > 0 and ladders > 0:
                        cache[index] = usingBricks = 1 + dft(heights, bricks -
                                                             (heights[index + 1] - heights[index]), ladders, index + 1, cache) + 1 + \
                            dft(heights, bricks, ladders - 1, index + 1, cache)
                    else:
                        cache[index] = 1 + \
                            dft(heights, bricks, ladders - 1, index + 1, cache)

            print(cache)
            return cache[index]
        return dft(heights, bricks, ladders, 0, {})


s = Solution()
s.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19],
                   10,
                   2)
