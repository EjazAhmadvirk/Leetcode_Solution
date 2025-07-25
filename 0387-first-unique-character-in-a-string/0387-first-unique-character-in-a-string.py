from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        Q = deque()

        for i in range(len(s)):
            if s[i] not in m:
                Q.append(i)
            m[s[i]] = m.get(s[i], 0) + 1

            while Q and m[s[Q[0]]] > 1:
                Q.popleft()

        return -1 if not Q else Q[0]

