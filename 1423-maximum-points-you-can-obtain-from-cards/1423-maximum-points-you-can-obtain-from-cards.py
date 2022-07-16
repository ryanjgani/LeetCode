class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        wlen = len(cardPoints) - k
        curSum = res = l = 0
        total = sum(cardPoints)
        for i in range(len(cardPoints)):
            if i >= wlen:
                res = max(total - curSum, res)
                curSum -= cardPoints[l]
                l += 1
            curSum += cardPoints[i]
        res = max(total - curSum, res)
        return res