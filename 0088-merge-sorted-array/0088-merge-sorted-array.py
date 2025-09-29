class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        # what if j=-1 already but k is not 0 yet? e.g. m=[1,2,0], n=[3]
        # => then no more ops needed, rest of m[] already sorted, so this while is good enough
        while j >= 0: 
            # i could be -1, eg. [7,8,9, ] and [1]
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1