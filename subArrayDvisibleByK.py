class Solution:
    def subarraysDivByK(self, A, K):

        total = 0
        seen = {}
        curr_total = 0
        for i in range(len(A)):
            curr_total += A[i]
            mod = curr_total % K
            if mod in seen:
                total += seen[mod]
                seen[mod] += 1

            else:
                seen[mod] = 1

            print(seen)
        return total + 1


s = Solution()
s.subarraysDivByK([4, 5, 0, -2, -3, 1],
                  5)
