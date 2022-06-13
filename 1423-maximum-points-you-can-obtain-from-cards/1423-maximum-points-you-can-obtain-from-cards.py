class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total
        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            res = max(res, total)
            r += 1
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