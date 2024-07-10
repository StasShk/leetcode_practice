### https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1

        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j], candies[j + 1] + 1)
        return sum(candies)