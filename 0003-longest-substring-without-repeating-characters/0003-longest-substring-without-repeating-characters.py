class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        min_len=1
        for i in range(n):
            for j in range(i+1,n+1):
                temp=s[i:j]
                s1=len(temp)
                res=len(set(temp))
                if s1==res:
                    if res>min_len:
                        min_len=res
                else:
                    break
        return min_len
        