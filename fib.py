class Solution:
    def fib(self, N: int, cache={}) -> int:
        if N == 0:
            return 0
        if N <= 2:
            return 1
        if N not in cache:
            cache[N] = self.fib(N - 1) + self.fib(N - 2)
        return cache[N]


s = Solution()
s.fib(10)
