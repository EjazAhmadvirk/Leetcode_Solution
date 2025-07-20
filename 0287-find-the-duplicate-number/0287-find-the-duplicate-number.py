class Solution:
    def findDuplicate(self, arr):
        slow = arr[0]
        fast = arr[0]

        # Phase 1: Detect the cycle
        while True:
            slow = arr[slow]            # +1 step
            fast = arr[arr[fast]]       # +2 steps
            if slow == fast:
                break

        # Phase 2: Find the entry point of the cycle (duplicate number)
        slow = arr[0]
        while slow != fast:
            slow = arr[slow]            # +1 step
            fast = arr[fast]            # +1 step

        return slow
