class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(s1) + 1):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]
        for i in range(1, len(s2) + 1):
            dp[0][i] = s2[i - 1] == s3[i - 1] and dp[0][i - 1]

        # fill in dp array
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                with_s1 = s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]
                with_s2 = s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]
                dp[i][j] = with_s1 or with_s2

        return dp[-1][-1]
