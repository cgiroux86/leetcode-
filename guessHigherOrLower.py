class Solution:
    def __init__(self, target):
        self.target = target

    def guess(self, n):
        if n == self.target:
            return 0
        if n < self.target:
            return -1
        if n > self.target:
            return 1

    def guessNumber(self, n):
        return self.binarySearch(n)

    def binarySearch(self, n):
        start = 0
        end = n
        while start < end:
            mid = (start + end) // 2
            if self.guess(mid) == -1:
                start = mid + 1
                continue
            if self.guess(mid) == 1:
                end = start + 1
                continue
            if self.guess(mid) == 0:
                return mid


s = Solution(6)
print(s.guessNumber(10))
