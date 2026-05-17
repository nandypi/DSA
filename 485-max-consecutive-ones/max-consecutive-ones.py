class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0 
        max_count = 0
        for n in nums:
            if n == 1:
                curr += 1
            else:
                max_count = max(curr, max_count)
                curr = 0
        max_count = max(curr, max_count)
        return max_count