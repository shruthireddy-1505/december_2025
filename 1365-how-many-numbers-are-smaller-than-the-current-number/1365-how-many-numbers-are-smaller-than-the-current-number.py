class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        dic={}
        sorted_list=sorted(nums)
        for i,v in enumerate(sorted_list):
            if v not in dic:
                dic[v]=i
        for v in range(len(nums)):
            temp=nums[v]
            ans[v]=dic[temp]
        return ans