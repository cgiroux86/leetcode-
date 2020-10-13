class Solution:
    def distributeCandies(self, candies, num_people):
        res = [0] * num_people
        candy_left = 1
        person = 0
        while candy_left <= candies:
            print(candies, candy_left)
            if person == len(res):
                person = 0
            res[person] += candy_left
            candies -= candy_left
            candy_left += 1
            person += 1
        res[person] += candies
        return res


s = Solution()
print(s.distributeCandies(7, 4))
