class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        length = len(s)
        dp = [0] * (length + 1) # dp[i] => at index i, its decode ways

        dp[length] = 1 # initiator, just make forloop flow working
        dp[length - 1] = 0 if s[length - 1] == '0' else 1 # assumption is starting at i, so starting as 0 is not decodable

        # start at 'len-2'
        # or else below 'dp[i+2]' will out of index boundary
        for i in range(length - 2, -1, -1):
            if s[i] == '0':
                continue
            tem = int(s[i:i + 2])

            if tem > 26:
                dp[i] = dp[i + 1]
            else:
                dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]
