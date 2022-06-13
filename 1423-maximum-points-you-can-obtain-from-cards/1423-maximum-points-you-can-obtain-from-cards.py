class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = 0
        N = len(cardPoints)
        l = 0
        curSum = 0
        total = sum(cardPoints)
        if k == N: return sum(cardPoints)
        
        for r in range(len(cardPoints)):
            curSum += cardPoints[r]
            
            # start sliding
            if r >= N - k - 1:
                print(curSum)
                res = max(res, total - curSum)
                curSum -= cardPoints[l] 
                l += 1
        return res
        
        
        # brute force O(2^n)
#         res = 0
#         dp = {}
        
#         def dfs(count, cards, curRes):
#             nonlocal res
#             if count == k:
#                 res = max(res, curRes)
#                 return
#             # left
#             left = cards.pop(0)
#             dfs(count + 1, cards[:], curRes + left)         
#             cards = [left] + cards  
            
#             # right
#             right = cards.pop()
#             dfs(count + 1, cards[:], curRes + right)
#             cards.append(right)
            
#         dfs(0, cardPoints, 0)
#         return res