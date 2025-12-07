class Solution:
    def countOdds(self, low: int, high: int) -> int:
        h=(1+high)//2
        l=(low)//2
        return h-l