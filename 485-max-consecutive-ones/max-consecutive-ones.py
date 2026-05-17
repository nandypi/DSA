class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = max_count = 0
        for n in nums:
            if n == 1:
                curr += 1
                max_count = max(curr, max_count)
            else:
                curr = 0
        return max_count