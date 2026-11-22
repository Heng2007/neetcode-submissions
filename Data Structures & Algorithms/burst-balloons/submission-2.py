class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        memo = {}
        def calc(l , r):
            if l>r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            best = 0
            for i in range(l, r+1):
                ans = nums[l-1]*nums[i]*nums[r+1]+calc(l,i-1)+calc(i+1,r)
                best = max(ans, best)
            memo[(l,r)] = best
            return best
        return calc(1,len(nums)-2 )            
            