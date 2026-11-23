class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = set(nums)
        sort = sorted(number)
        #edge cases
        if len(nums) == 0:
            return 0
        best = 0
        count = 1
        for i in sort:
            if i+1 in number:
                count += 1
            else:
                best = max(best, count)
                count = 1
        best = max(best,count)
        return best
            