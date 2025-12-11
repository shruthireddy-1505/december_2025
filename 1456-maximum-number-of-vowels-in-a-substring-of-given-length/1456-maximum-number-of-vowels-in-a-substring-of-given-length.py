class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d={}
        for i in s:
            if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O'or i=='u' or i=='U':
                d[i]=1
            else:
                d[i]=0
        max_val=float('-inf')
        count=0

        for i in range(k):
            if s[i] in d:
                count+=d[s[i]]
            max_val=count
        for i in range(k,len(s)):
            count+=d[s[i]]
            rem=i-k
            count-=d[s[rem]]
            
            max_val=max(count,max_val)
        return max_val
                