class Solution:
  def lengthOfLongestSubstring(self, s): # map for index
    d = {} # value => its index
    i = 0
    ans = 0
    for j, c in enumerate(s):
      if c in d:
        # mast max check i, example "abba"
        i = max(i, d[c] + 1)
      d[c] = j
      ans = max(ans, j - i + 1)
    return ans
