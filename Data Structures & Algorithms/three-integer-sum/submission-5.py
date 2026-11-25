class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                summation = nums[i]+nums[l]+nums[r]
                if summation >0:
                    r-=1
                elif summation<0:
                    l+=1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1
                    while nums[r] == nums[r+1] and r>l:
                        r-=1
                 
        return result