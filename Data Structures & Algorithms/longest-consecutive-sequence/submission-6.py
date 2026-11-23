class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = set(nums)
        if len(nums) == 0 :
            return 0
        best = 0
        count = 0
        n = 0
        for element in number:
            if element-1 not in number:
                while element + n in number:
                    n += 1
                    count += 1
                
            best = max(count, best)
            n = 0
            count = 0
        return best

                





            