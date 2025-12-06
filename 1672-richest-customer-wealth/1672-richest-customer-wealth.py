class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n=len(accounts)
        m=len(accounts[0])
        max_count=0
        for i in range(n):
            sum_x=0
            for j in range(m):
                sum_x+=accounts[i][j]
            max_count=max(max_count,sum_x)
        return max_count
        