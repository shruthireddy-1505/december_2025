class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[0]*len(nums)
        even=0
        odd=1
        for i in range(len(nums)):
            if i<n:
                ans[even]=nums[i]
                even+=2
            else:
                ans[odd]=nums[i]
                odd+=2
        return ans
