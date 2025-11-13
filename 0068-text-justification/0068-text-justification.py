class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        left = 0
        result = []
        
        while left < len(words):
            right = self.findRight(left, words, maxWidth)
            result.append(self.justify(left, right, words, maxWidth))
            left = right + 1
        
        return result
    
    def findRight(self, left, words, maxWidth):
        right = left
        word_length = len(words[right])
        
        while (right + 1) < len(words) and (word_length + 1 + len(words[right+1])) <= maxWidth:
            right += 1
            word_length += 1 + len(words[right])
        
        return right
    
    def justify(self, left, right, words, maxWidth):
        if right - left == 0:
            return self.padResult(words[left], maxWidth)
        
        is_last_line = (right == len(words) - 1)
        num_spaces = right - left
        total_space = maxWidth - self.wordsLength(left, right, words)
        
        space = " " if is_last_line else " " * (total_space // num_spaces)
        remainder = 0 if is_last_line else total_space % num_spaces
        
        result = ""
        for i in range(left, right):
            result += words[i]
            result += space
            if remainder > 0:
                result += " "
                remainder -= 1
        
        result += words[right]
        result += " " * (maxWidth - len(result))
        
        return result
    
    def wordsLength(self, left, right, words):
        words_length = 0
        for i in range(left, right+1):
            words_length += len(words[i])
        return words_length
    
    def padResult(self, result, maxWidth):
        return result + " " * (maxWidth - len(result))

