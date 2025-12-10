class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start = 0
        ans = ""
        n = len(s)

        
        if k == 0:
            return s
        if n <= k:
            return s[::-1]

        while start < n:
            rem = n - start

            if rem >= 2 * k:
                ans += s[start:start + k][::-1]
                ans += s[start + k:start + 2 * k]
                start += 2 * k

            elif rem > k:
                ans += s[start:start + k][::-1]
                ans += s[start + k:]
                break

            else:
                ans += s[start:][::-1]
                break

        return ans