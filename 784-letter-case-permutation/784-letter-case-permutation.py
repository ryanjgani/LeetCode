class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # BFS solution - iterative
        # res = [s]
        # for i in range(len(s)):
        #     temp = []
        #     if s[i].isalpha():
        #         while res:
        #             string = res.pop(0)
        #             left = string[:i]
        #             right = string[i + 1:]
        #             temp.append(left + s[i].upper() + right)
        #             temp.append(left + s[i].lower() + right)
        #         res = temp
        # return res
        
        # DFS solution - recursive
        res = []
        
        def dfs(sub, i):
            if i >= len(s):
                res.append(sub[:])
                return
            if s[i].isalpha():
                # swap
                dfs(sub + s[i].lower(), i + 1)
                dfs(sub + s[i].upper(), i + 1)
            else:
                dfs(sub + s[i], i + 1)

        dfs("", 0)
        return res