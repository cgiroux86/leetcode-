
def numSubarraysWithSum(A, S):
    res = 0
    sub = 0
    for i in range(len(A)):
        sub = A[i]
        if sub == S:
            res += 1
        for j in range(i + 1, len(A)):
            sub = sub + A[j]
            if sub == S:
                res += 1
            if sub > S:
                break
    return res


numSubarraysWithSum([0, 0, 0, 0, 0], 0)
