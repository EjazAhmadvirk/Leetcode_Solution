class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]  # Reverse the entire string
        n = len(s)
        i = 0
        ans = ""

        while i < n:
            word = ""
            while i < n and s[i] != ' ':
                word += s[i]
                i += 1

            word = word[::-1]  # Reverse the word
            if len(word) > 0:
                ans += " " + word

            # Skip spaces
            while i < n and s[i] == ' ':
                i += 1

        return ans[1:]  # Remove the leading space
