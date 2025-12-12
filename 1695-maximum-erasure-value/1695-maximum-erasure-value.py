class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res=set()
        max_val=0
        sum_val=0
        j=0
        for i in range(len(nums)):
            while nums[i] in res:
                res.remove(nums[j])
                sum_val-=nums[j]
                j+=1
            res.add(nums[i])
            sum_val+=nums[i]
            max_val=max(max_val,sum_val)
        return max_val