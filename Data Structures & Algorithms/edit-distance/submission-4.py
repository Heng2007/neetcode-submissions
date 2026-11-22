class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def calc(i , j):
            if i == len(word1):
                return len(word2)- j
            if j == len(word2):
                return len(word1) - i
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                ans =  calc(i+1, j+1)
            else:
                ans =  1+ min(calc(i+1, j), calc(i, j+1), calc(i+1, j+1))
            memo [i, j] = ans
            return ans
        return calc(0, 0)