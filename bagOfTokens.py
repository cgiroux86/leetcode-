class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = tokens.sort()
        total = 0
        if P >= tokens[0] and total < 1:
            total += 1
            P -= tokens[0]
        else:
            total += max(self.bagOfTokensScore(tokens[1:], P += tokens[0]))

    [100, 200, 300, 400, 500] 500
    400 1 [200, 300, 400, 500]
    600 0 [300, 400, 500]
    300 1 [4]
