class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        res=float('inf')
        min_diff=float('inf')

        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue

            j=i+1
            k=n-1
            while j<k:
                add=nums[i]+nums[j]+nums[k]
                diff=abs(add-target)
                if add==target:
                    return target
                if diff<min_diff:
                    res=add
                    min_diff=diff
                if add>target:
                    k-=1
                elif add<target:
                    j+=1
        return res
                    
            