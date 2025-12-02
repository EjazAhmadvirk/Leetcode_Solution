class Solution: # also passing OJ by switching a/b
  def getSum(self, a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    kMax = 0x80000000
    # the result of each step is passed recursively to the getSum function
    # until there is no carry (b == 0)
    # at that point, the function returns the final sum.
    while b:
      a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    return a if a < kMax else ~(a ^ mask)