function letterCombinations(digits: string): string[] {
  if (digits.length === 0) return [];

  const phoneMap: Record<string, string> = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
  };

  const result: string[] = [];

  function backtrack(index: number, current: string) {
    if (index === digits.length) {
      result.push(current);
      return;
    }

    for (const letter of phoneMap[digits[index]]) {
      backtrack(index + 1, current + letter);
    }
  }

  backtrack(0, "");
  return result;
}

// Example usage
console.log(letterCombinations("23"));
