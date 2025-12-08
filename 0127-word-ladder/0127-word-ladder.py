# native BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        q = deque([beginWord])
        ans = 1
        while q:
            ans += 1
            for _ in range(len(q)):
                s = q.popleft()
                s = list(s) # must convert to list, cannot directly update s[i]='a'
                for i in range(len(s)):
                    ch = s[i]
                    for j in range(26):
                        # will re-generate s itself
                        # but s not in words-set, s removed after added to words-set
                        s[i] = chr(ord('a') + j)
                        t = ''.join(s)
                        if t not in words:
                            continue
                        if t == endWord:
                            return ans
                        q.append(t)
                        words.remove(t) # equivalent to set t as visited
                    s[i] = ch # restore
        return 0

