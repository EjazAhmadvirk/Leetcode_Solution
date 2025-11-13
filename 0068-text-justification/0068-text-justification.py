'''
>>> 17 % 3
2
>>> divmod(17,3)
(5, 2)
'''

'''
>>> ['This', 'is', 'an']
['This', 'is', 'an']
>>> t = ['This', 'is', 'an']
>>> spaces = ['    ', '    ']

# note: here j starts from 0
>>> for j, word in enumerate(t[1:]):
...     print(j)
...     print(word)
...
0
is
1
an
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def partition(n, cnt):
            base, mod = divmod(n, cnt)
            res = [f"{' ' * (base + (i < mod))}" for i in range(cnt)]
            return res

        ans = []
        i, n = 0, len(words)
        while i < n: # one line per iteration
            t = [words[i]]
            cnt = len(words[i])
            i += 1 # move to next word
            while i < n and cnt + 1 + len(words[i]) <= maxWidth: # greedy search for one line
                cnt += 1 + len(words[i])
                t.append(words[i])
                i += 1
            if i == n or len(t) == 1:
                # this is the last line or only one (super-long) word in a line
                left = ' '.join(t)
                right = ' ' * (maxWidth - len(left))
                ans.append(f"{left}{right}")
                continue # so i != n , so only one word, no need to add spaces. 
                         # e.g. a word with the same length as maxWidth, 
                         # or, e.g. the 2nd word is super long and cannot fit in current line
                # if i==n, then will not enter next while
            words_width = cnt - (len(t) - 1) # pure words total length, with no spaces
                                             # spaces in-between these words in t[]: len(t) - 1
            space_width = maxWidth - words_width
            spaces = partition(space_width, len(t) - 1)
            sb = [t[0]] # 1st word of this line, no space before it
            for j, word in enumerate(t[1:]): # last word has no following space
                sb.append(spaces[j]) # j starts from 0
                sb.append(word)
            ans.append(''.join(sb))
        return ans
